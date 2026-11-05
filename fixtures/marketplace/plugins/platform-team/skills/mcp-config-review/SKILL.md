---
name: mcp-config-review
description: Review an agent's MCP server configuration and permissions before the agent is rolled out. Use it when someone adds an MCP server, changes an agent's tools or asks whether an agent setup is safe.
license: Apache-2.0
version: "1.0.0"
publisher: Example Freight platform team
---

# MCP configuration review

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Before you start

1. Ask which agent the configuration is for, who uses it, and what the agent must be able to do.
2. List every MCP server the configuration starts or connects to, and every tool each one offers.

## Check each server

- **Source.** A local server runs a package pinned to a version from a known index. A remote server is reached over HTTPS at a host the team runs or has chosen.
- **Credentials.** Keys and tokens come from the environment or a secret store, never written into the file, and each one has only the access the agent needs.
- **Approval.** Tools that write, delete, send or spend wait for a person to approve the call. Automatic approval is only for tools that read.
- **Scope.** A database or cluster server runs read-only unless the task needs writes, and then only on the data the task names.
- **Tool text.** Tool names and descriptions say what the tool does and nothing else. A description that gives the agent instructions is a finding.

## Report

For each server, give what it can reach, what it can change without a person, and what to tighten. End with the changes that matter most.
