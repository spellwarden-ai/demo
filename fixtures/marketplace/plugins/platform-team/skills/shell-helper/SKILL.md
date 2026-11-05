---
name: shell-helper
description: Run the shell commands a platform task needs, such as checking disk space or tailing a service log. Use it when someone asks for a quick look at a server.
license: Apache-2.0
version: "1.0.2"
publisher: Example Freight platform team
allowed-tools: Read, Grep, Bash
---

# Shell helper

This is a demo skill of the fictional company Example Freight. Its problem is deliberate: the Spellwarden live demo shows what a scan finds in it. Do not install it.

Its frontmatter pre-approves the shell with no scope, so the agent may run any command without asking. A safer skill names the one command it needs, such as `Bash(df -h)`.

## Look at the server

1. Ask which host and which service the question is about.
2. Check the free disk space and the last lines of the service's log.
3. Report what you found in two or three lines.
