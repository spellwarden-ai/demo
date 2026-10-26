---
name: release-notes-writer
description: Write release notes from the merged pull requests since the last tag. Use it when a release is being prepared or when someone asks what changed in a version.
license: Apache-2.0
version: "1.0.3"
publisher: Example Freight platform team
---

# Release notes writer

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Collect the changes

```sh
git describe --tags --abbrev=0
git log --merges --first-parent --format='%s' "$(git describe --tags --abbrev=0)"..HEAD
```

## Write the notes

- Group the changes under "New", "Changed" and "Fixed".
- One line per change, in plain words a customer understands, without internal ticket numbers.
- Name every change that needs the reader to do something first, under "Before you upgrade".

Show the draft to the user and change it as they ask before it is published.
