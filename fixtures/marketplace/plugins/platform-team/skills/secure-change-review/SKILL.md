---
name: secure-change-review
description: Review a code change for security problems before it is merged. Use it when someone asks for a security review of a pull request, a diff or a new endpoint.
license: Apache-2.0
version: "1.0.0"
publisher: Example Freight platform team
---

# Secure change review

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Before you read the change

1. Ask what the change is for and who can reach the code it touches: the public, signed-in users, staff or other services.
2. Read the whole diff, not only the files named in the request.

## Read the change

- **Input.** Every value that comes from a request, a file, a queue or another service is untrusted until it is checked. Look for it reaching a query, a shell command, a file path, a template or a redirect.
- **Access.** Each new route or action checks who is asking and whether they may act on that record, not only whether they are signed in.
- **Secrets.** No key, token or password is added to the code, the tests or the logs.
- **Errors.** An error answer tells the caller what went wrong without stack traces, queries or internal names.
- **Dependencies.** A new package is pinned to a version, and the reason for it is in the change.
- **Data.** Personal data that the change stores or sends is the least the feature needs.

## Report

List each problem with the file and line, why it matters, and a fix. Say plainly when you found none, and what you did not check.
