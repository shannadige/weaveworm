#!/usr/bin/env python3
"""PreToolUse guard shipped with every weaveworm plugin.

Project artifacts live under the working directory. The plugin checkout
(this plugin's folder and the folder above it, which also has stage-named
subfolders) holds only spec, voice, and skill files. A Read, Glob, Grep, or
Bash path that reaches into that checkout anywhere other than a
`references/` or `skills/` folder is denied with one line the model can
act on. Paths under the working directory are always allowed, so a project
that happens to live inside the checkout is never blocked. Any failure in
this script allows the call (fail open); it must never break a session.
"""
import json, os, re, sys


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name") or ""
    inp = data.get("tool_input") or {}
    cwd = os.path.realpath(data.get("cwd") or os.getcwd())
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.realpath(os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.join(here, ".."))
    parent = os.path.dirname(root)
    if not parent or parent == os.sep:
        return

    def resolve(p):
        p = os.path.expanduser(p)
        if not os.path.isabs(p):
            p = os.path.join(cwd, p)
        return os.path.realpath(p)

    def under(p, base):
        return p == base or p.startswith(base + os.sep)

    def is_reach(p):
        p = resolve(p)
        if under(p, cwd):
            return False
        if not under(p, parent):
            return False
        parts = [x for x in os.path.relpath(p, parent).split(os.sep) if x and x != "."]
        if parts and parts[0] == "references":
            return False
        if len(parts) >= 2 and parts[1] in ("references", "skills"):
            return False
        return True

    candidates = []
    if tool in ("Read", "Glob", "Grep"):
        for key in ("file_path", "path"):
            if isinstance(inp.get(key), str) and inp[key]:
                candidates.append(inp[key])
        if tool == "Glob" and isinstance(inp.get("pattern"), str) and os.path.isabs(inp["pattern"]):
            candidates.append(inp["pattern"])
    elif tool == "Bash":
        cmd = inp.get("command") or ""
        for m in re.finditer(re.escape(parent) + r"(?:/[^\s\"'`;|&<>()]*)?", cmd):
            candidates.append(m.group(0))
    else:
        return

    hits = [c for c in candidates if is_reach(c)]
    if not hits:
        return
    shown = hits[0] if len(hits) == 1 else f"{hits[0]} (and {len(hits) - 1} more)"
    reason = (f"{shown} is inside the plugin checkout, which holds only spec and skill files; "
              f"project files live under the working directory ({cwd}), so use a relative path "
              f"like research/, define/, design/, or deliver/ from there.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": "deny",
                                             "permissionDecisionReason": reason}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: fail open
        pass
    sys.exit(0)
