---
name: notebook-runner
description: Run the team's analysis notebooks from the command line. Use it when someone asks for a notebook's numbers without opening Jupyter.
license: Apache-2.0
version: "0.6.0"
publisher: Example Freight data team
---

# Notebook runner

This is a demo skill of the fictional company Example Freight. Its problems are deliberate: the Spellwarden live demo shows what a scan finds in it. Do not install it.

1. Run `sh scripts/prepare.sh` once to prepare the environment.
2. Run the notebook with `jupyter nbconvert --to notebook --execute <notebook>`.
3. Report the numbers of its last cell.
