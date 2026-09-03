#!/usr/bin/env python3
"""Plugin-root guard shipped with every weaveworm plugin.

Project artifacts live under the working directory. The plugin checkout
(this plugin's folder and the folder above it, which also has stage-named
subfolders) holds only spec, voice, and skill files. Two hook events, one
script:

PreToolUse (Read, Glob, Grep, Bash): a path that reaches into that
checkout anywhere other than a `references/` or `skills/` folder is
denied with one line the model can act on. Paths under the working
directory are always allowed, so a project that happens to live inside the
checkout is never blocked.

PostToolUse (Skill): the moment a skill loads is the moment the model
first sees the plugin's absolute path, so one line of context names the
working directory the project lives under and the two folders in the
checkout that are readable.

Any failure in this script allows the call (fail open); it must never
break a session.
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

    def under(p, base):
        return p == base or p.startswith(base + os.sep)

    if not parent or parent == os.sep:
        return
    event = data.get("hook_event_name") or ""

    if event == "PostToolUse":
        if tool != "Skill" or under(cwd, parent):
            return
        context = (f"Project artifacts (research/, define/, design/, deliver/) live under the working "
                   f"directory {cwd}; read and write them by relative paths from there. The plugin "
                   f"checkout at {parent} is not the project: only {root}/references/ and "
                   f"{root}/skills/ are readable there, and every other path in it is denied.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                                 "additionalContext": context}}))
        return

    def resolve(p):
        p = os.path.expanduser(p)
        if not os.path.isabs(p):
            p = os.path.join(cwd, p)
        return os.path.realpath(p)

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
