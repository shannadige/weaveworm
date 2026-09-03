#!/usr/bin/env python3
"""Stand-in runner for `claude plugin eval` while that command is gated.

Reads the same case layout (`<plugin>/evals/<case>/prompt.md`, `graders/*.md`,
`case.yaml`) and runs each case in a fresh workspace through headless
`claude -p`, in up to three arms:

  without  no plugin, no extra prompt            (raw prompting)
  spec     define-spec.md appended as system prompt (a strong prompt, no skill)
  with     the plugin loaded via --plugin-dir     (the skill)

File-targeted graders see files the agent created OR modified in the workspace.
Deterministic graders (file_exists, regex, tool_used) run locally; llm graders
call a judge model with structured output. Graders marked `with_only: true`
are reported but excluded from the score, matching the official ablation.
`--skip-llm` skips the judge entirely (llm graders are reported as skipped and
excluded from the score); that is the smoke configuration `scripts/smoke.sh` uses.

Usage:
  scripts/eval-pilot.py define [--case journey-map-basic] [--runs 2]
      [--arms without,spec,with] [--model sonnet] [--judge-model sonnet]
      [--parallel 4] [--out define/evals/results] [--skip-llm]
"""
import argparse, codecs, concurrent.futures as cf, datetime as dt, fnmatch, glob, json, os, re
import shutil, subprocess, sys, tempfile, threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCK = threading.Lock()

# ---------- minimal frontmatter (flat keys, one nesting level, [a, b] lists) ----------
def parse_scalar(v):
    v = v.strip()
    if v.startswith('[') and v.endswith(']'):
        return [parse_scalar(x) for x in v[1:-1].split(',') if x.strip()]
    if v.startswith('"') and v.endswith('"'):
        return v[1:-1].encode('latin-1', 'backslashreplace').decode('unicode_escape')
    if v.startswith("'") and v.endswith("'"):
        return v[1:-1]
    if v in ('true', 'false'):
        return v == 'true'
    if re.fullmatch(r'-?\d+', v):
        return int(v)
    return v

def parse_frontmatter(text):
    if not text.startswith('---'):
        return {}, text
    _, fm, body = text.split('---', 2)
    data, cur = {}, None
    for line in fm.splitlines():
        if not line.strip():
            continue
        if line.startswith('  ') and cur:
            k, v = line.strip().split(':', 1)
            data[cur][k.strip()] = parse_scalar(v)
        else:
            k, v = line.split(':', 1)
            k = k.strip()
            if v.strip() == '':
                data[k], cur = {}, k
            else:
                data[k], cur = parse_scalar(v), None
    return data, body.strip()

def load_case(case_dir):
    fm, body = parse_frontmatter(open(os.path.join(case_dir, 'prompt.md')).read())
    graders = []
    for g in sorted(glob.glob(os.path.join(case_dir, 'graders', '*.md'))):
        gfm, gbody = parse_frontmatter(open(g).read())
        gfm['name'], gfm['body'] = os.path.basename(g)[:-3], gbody
        graders.append(gfm)
    scaffold = None
    cy = os.path.join(case_dir, 'case.yaml')
    if os.path.exists(cy):
        m = re.search(r'scaffold_script:\s*(\S+)', open(cy).read())
        if m:
            scaffold = os.path.abspath(os.path.join(case_dir, m.group(1)))
    return dict(name=fm.get('name', os.path.basename(case_dir)), prompt=body,
                runs=fm.get('runs', 3), max_turns=fm.get('max_turns', 10),
                allowed_tools=fm.get('allowed_tools', ['Read']), graders=graders,
                scaffold=scaffold, dir=case_dir)

# ---------- running one arm ----------
def run_agent(case, arm, model, plugin_dir, spec_file, workspace):
    if case['scaffold']:
        subprocess.run(['bash', case['scaffold']], cwd=workspace, check=True,
                       env={**os.environ, 'EVAL_CASE_DIR': case['dir']})
    before = snapshot(workspace)
    cmd = ['claude', '-p', case['prompt'], '--model', model,
           '--max-turns', str(case['max_turns']), '--setting-sources', 'project',
           '--permission-mode', 'acceptEdits',
           '--allowedTools', *[t for t in case['allowed_tools'] if t not in ('Write', 'Edit')],
           '--output-format', 'stream-json', '--verbose']
    if arm == 'with':
        cmd += ['--plugin-dir', plugin_dir]
    elif arm == 'spec':
        cmd += ['--append-system-prompt-file', spec_file]
    env = {k: v for k, v in os.environ.items() if k not in ('CLAUDECODE',)}
    proc = subprocess.run(cmd, cwd=workspace, capture_output=True, text=True, env=env,
                          timeout=1200, stdin=subprocess.DEVNULL)
    tool_uses, last_text, result = [], '', {}
    for line in proc.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get('type') == 'assistant':
            texts = []
            for blk in ev.get('message', {}).get('content', []):
                if blk.get('type') == 'tool_use':
                    tool_uses.append({'name': blk.get('name'), 'input': blk.get('input')})
                elif blk.get('type') == 'text':
                    texts.append(blk.get('text', ''))
            if texts:
                last_text = '\n'.join(texts)
        elif ev.get('type') == 'result':
            result = ev
    after = snapshot(workspace)
    created = sorted(f for f, sig in after.items() if before.get(f) != sig)  # created or modified
    outside = sorted({u['input'].get('file_path', '') for u in tool_uses
                      if u['name'] in ('Write', 'Edit') and isinstance(u['input'], dict)
                      and not os.path.realpath(os.path.join(workspace, u['input'].get('file_path', ''))).startswith(os.path.realpath(workspace))})
    return dict(tool_uses=tool_uses, wrote_outside=outside, last_message=result.get('result') or last_text,
                created=created, cost=result.get('total_cost_usd'),
                turns=result.get('num_turns'), duration_ms=result.get('duration_ms'),
                exit=proc.returncode, stderr=proc.stderr[-2000:], trace=proc.stdout)

def all_files(root):
    for d, _, fs in os.walk(root):
        for f in fs:
            yield os.path.relpath(os.path.join(d, f), root)

def snapshot(root):
    out = {}
    for f in all_files(root):
        st = os.stat(os.path.join(root, f))
        out[f] = (st.st_size, st.st_mtime_ns)
    return out

# ---------- grading ----------
def target_text(grader, run, workspace):
    t = grader.get('target', 'last_message')
    if t == 'last_message':
        return run['last_message']
    if t == 'trace':
        return run['trace']
    if isinstance(t, dict) and t.get('source') == 'file':
        hits = [f for f in run['created'] if fnmatch.fnmatch(f, t['path'])]
        if not hits:
            return None
        return '\n\n'.join(open(os.path.join(workspace, h)).read() for h in hits)
    return run['last_message']

def judge(judge_model, criteria, content):
    schema = json.dumps({'type': 'object', 'properties': {
        'pass': {'type': 'boolean'}, 'reason': {'type': 'string'}},
        'required': ['pass', 'reason']})
    prompt = ('You are grading the output of an AI assistant against fixed criteria. '
              'Be strict: pass only if every numbered point holds. Give a one-sentence '
              'reason naming the first failing point, or what satisfied all points.\n\n'
              f'CRITERIA:\n{criteria}\n\nOUTPUT TO GRADE:\n<<<\n{content}\n>>>')
    env = {k: v for k, v in os.environ.items() if k not in ('CLAUDECODE',)}
    p = subprocess.run(['claude', '-p', prompt, '--model', judge_model, '--max-turns', '4',
                        '--setting-sources', 'project', '--output-format', 'json',
                        '--json-schema', schema], capture_output=True, text=True, env=env,
                       cwd=tempfile.gettempdir(), timeout=300, stdin=subprocess.DEVNULL)
    try:
        d = json.loads(p.stdout)
        if d.get('is_error'):
            return False, f"judge error: {d.get('subtype')}", d.get('total_cost_usd', 0)
        so = d.get('structured_output') or json.loads(d.get('result', '{}'))
        return bool(so.get('pass')), so.get('reason', ''), d.get('total_cost_usd', 0)
    except Exception as e:  # noqa
        return False, f'judge error: {e}: {p.stdout[-300:]} {p.stderr[-300:]}', 0

def grade(grader, run, workspace, judge_model, skip_llm=False):
    t = grader['type']
    if t == 'llm' and skip_llm:
        return None, 'skipped (--skip-llm)', 0
    if t == 'file_exists':
        ok = any(fnmatch.fnmatch(f, grader['path']) for f in run['created'])
        return ok, ('found' if ok else 'no created file matches ' + grader['path']), 0
    if t == 'regex':
        text = target_text(grader, run, workspace)
        if text is None:
            return False, 'target file missing', 0
        flags = re.M if 'm' in str(grader.get('flags', '')) else 0
        if 'i' in str(grader.get('flags', '')):
            flags |= re.I
        n = len(re.findall(grader['pattern'], text, flags))
        mode = grader.get('match', 'contains')
        ok = n > 0 if mode == 'contains' else n == 0
        return ok, f'{n} match(es), wanted {mode}', 0
    if t == 'tool_used':
        pat = grader.get('input_match')
        hits = [u for u in run['tool_uses'] if u['name'] == grader['tool']
                and (not pat or re.search(pat, json.dumps(u['input'])))]
        lo, hi = grader.get('min', 1), grader.get('max', 10**6)
        return lo <= len(hits) <= hi, f'{len(hits)} call(s)', 0
    if t == 'llm':
        text = target_text(grader, run, workspace)
        if text is None:
            return False, 'target file missing', 0
        return judge(judge_model, grader['body'], text)
    return False, f'unsupported grader type {t}', 0

# ---------- orchestration ----------
def one_run(case, arm, i, args, spec_file, out_dir):
    ws = tempfile.mkdtemp(prefix=f'{case["name"]}-{arm}-{i}-', dir=args.tmp)
    try:
        run = run_agent(case, arm, args.model, args.plugin_dir, spec_file, ws)
        results, cost = [], run['cost'] or 0
        for g in case['graders']:
            ok, why, jc = grade(g, run, ws, args.judge_model, args.skip_llm)
            cost += jc
            results.append(dict(grader=g['name'], type=g['type'], passed=ok, reason=why,
                                with_only=bool(g.get('with_only')), skipped=ok is None))
        scored = [r for r in results if not r['with_only'] and not r['skipped']]
        score = sum(r['passed'] for r in scored) / max(1, len(scored))
        keep = os.path.join(out_dir, 'runs', f'{case["name"]}', f'{arm}-{i}')
        os.makedirs(keep, exist_ok=True)
        for f in run['created']:
            dst = os.path.join(keep, 'created', f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(os.path.join(ws, f), dst)
        open(os.path.join(keep, 'last_message.md'), 'w').write(run['last_message'])
        open(os.path.join(keep, 'trace.jsonl'), 'w').write(run['trace'])
        with LOCK:
            flag = '  WROTE OUTSIDE WORKSPACE: ' + ', '.join(run['wrote_outside']) if run['wrote_outside'] else ''
            print(f'  {case["name"]:32s} {arm:8s} run {i}: score {score:.2f}  '
                  f'turns {run["turns"]}  ${cost:.2f}{flag}', flush=True)
        return dict(case=case['name'], arm=arm, run=i, score=score, graders=results,
                    cost=cost, turns=run['turns'], duration_ms=run['duration_ms'],
                    created=run['created'], wrote_outside=run['wrote_outside'],
                    exit=run['exit'], stderr=run['stderr'])
    finally:
        shutil.rmtree(ws, ignore_errors=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('plugin')
    ap.add_argument('--case', default='*')
    ap.add_argument('--runs', type=int)
    ap.add_argument('--arms', default='without,spec,with')
    ap.add_argument('--model', default='sonnet')
    ap.add_argument('--judge-model', default='sonnet')
    ap.add_argument('--parallel', type=int, default=4)
    ap.add_argument('--out')
    ap.add_argument('--tmp', default=tempfile.gettempdir())
    ap.add_argument('--skip-llm', action='store_true', help='skip llm graders (no judge calls)')
    args = ap.parse_args()
    args.plugin_dir = os.path.abspath(args.plugin)
    eval_dir = os.path.join(args.plugin_dir, 'evals')
    specs = glob.glob(os.path.join(args.plugin_dir, 'references', '*-spec.md'))
    spec_file = specs[0] if specs else None
    if 'spec' in args.arms.split(',') and not spec_file:
        sys.exit('spec arm needs <plugin>/references/*-spec.md')
    cases = [load_case(d) for d in sorted(glob.glob(os.path.join(eval_dir, args.case)))
             if os.path.exists(os.path.join(d, 'prompt.md'))]
    if not cases:
        sys.exit('no cases')
    ts = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    out_dir = os.path.abspath(args.out or os.path.join(eval_dir, 'results', ts))
    os.makedirs(out_dir, exist_ok=True)
    arms = args.arms.split(',')
    jobs = [(c, a, i) for c in cases for a in arms for i in range(args.runs or c['runs'])]
    print(f'{len(cases)} case(s) x {arms} -> {len(jobs)} runs, model={args.model}, '
          f'judge={args.judge_model}\nresults: {out_dir}', flush=True)
    with cf.ThreadPoolExecutor(args.parallel) as ex:
        futs = [ex.submit(one_run, c, a, i, args, spec_file, out_dir) for c, a, i in jobs]
        runs = [f.result() for f in futs]

    # aggregate
    agg = {}
    for c in cases:
        agg[c['name']] = {}
        for a in arms:
            rs = [r for r in runs if r['case'] == c['name'] and r['arm'] == a]
            per_grader = {}
            for g in c['graders']:
                hits = [gr['passed'] for r in rs for gr in r['graders']
                        if gr['grader'] == g['name'] and not gr.get('skipped')]
                per_grader[g['name']] = sum(hits) / len(hits) if hits else None
            agg[c['name']][a] = dict(mean_score=sum(r['score'] for r in rs) / max(1, len(rs)),
                                     runs=len(rs), cost=sum(r['cost'] for r in rs),
                                     graders=per_grader)
    json.dump(dict(suite=os.path.basename(args.plugin_dir), model=args.model,
                   judge_model=args.judge_model, arms=arms, cases=agg, runs=runs),
              open(os.path.join(out_dir, 'aggregate-result.json'), 'w'), indent=2)

    lines = [f'# eval pilot {ts}', '', f'model {args.model}, judge {args.judge_model}, '
             f'{sum(r["cost"] for r in runs):.2f} USD total', '']
    for cname, byarm in agg.items():
        lines += [f'## {cname}', '', '| grader | ' + ' | '.join(arms) + ' |',
                  '|---|' + '---|' * len(arms)]
        for g in cases[[c['name'] for c in cases].index(cname)]['graders']:
            tag = ' (indicator)' if g.get('with_only') else ''
            lines.append(f'| {g["name"]}{tag} | ' + ' | '.join(
                'skipped' if byarm[a]["graders"][g["name"]] is None
                else f'{byarm[a]["graders"][g["name"]]:.2f}' for a in arms) + ' |')
        lines.append('| **mean score** | ' + ' | '.join(
            f'**{byarm[a]["mean_score"]:.2f}**' for a in arms) + ' |')
        lines.append('')
    open(os.path.join(out_dir, 'summary.md'), 'w').write('\n'.join(lines))
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
