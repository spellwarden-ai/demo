# Spellwarden live demo: fixtures

This repository holds the fixtures of the Spellwarden live demo at https://dash.spellwarden.ai/live-demo: agent skills, MCP client configurations, Claude Code settings and A2A agent cards of a fictional freight company, Example Freight. Some are clean and some have problems put there on purpose. The demo organisation imports the skills and the MCP configuration from this repository, and this repository's workflow scans it in connected mode into that organisation, so the demo shows what Spellwarden finds and how a team works through it.

**Every problem in this repository is deliberate and inert. Do not install these skills or plugins, do not add these marketplaces, and do not open any directory under `fixtures/projects/` as a project in Claude Code, VS Code or Cursor.**

## Why it is safe to clone

- **Network targets.** Every address in the fixtures is a host under `.invalid` (which never resolves), under `example.com` or `example.org`, a documentation address (`203.0.113.0/24`), or one of Spellwarden's own demo MCP endpoints under `demo-mcp.spellwarden.ai`, which answer every tool call with "This is a demo server. It does nothing." and keep nothing a request sends. The cloud metadata address `169.254.169.254` appears only inside a sentence of a skill, never in a command.
- **Package installs** name `.invalid` package indexes, so nothing is downloaded.
- **Encoded payloads** decode to `echo demo` and nothing else.
- **Credentials** are visibly fake (`hunter2hunter2`, `demo-literal-123`, `not-a-real-key-1`, `not-a-real-password`) and have the shape of no provider's token.
- **Nothing loads from the root.** There is no `.claude/`, `.mcp.json` or `.claude-plugin/` at the root. Claude Code reads project settings only from the root `.claude/` of the folder it is opened in, so cloning this repository and opening it loads none of the settings fixtures, and `/plugin marketplace add spellwarden-ai/demo` finds no marketplace.
- **Every plugin** says so first: each description starts with "Demo fixture with deliberate problems. Do not install."

Someone who installs a fixture skill anyway and follows it fetches from `.invalid` hosts (no address answers), decodes `echo demo` and removes a directory under `$TMPDIR`. The skills that try to steer an agent ask it to add a line to replies or to send messages to a fictional agent first; nothing they point at does harm.

## Layout

```
README.md                  this file: what the repository is, and the rule ids each fixture is recorded with
SEED.md                    the seed record: tag, date, the public registry servers chosen, the counts captured
LICENSE                    Apache-2.0
.github/workflows/         spellwarden.yml (the scan in connected mode) and check.yml (this repository's own checks)
.spellwarden/config.yml    the settings of the scan: never fail, no probe, no telemetry; no baseline, nothing suppressed
tools/                     check_repo.py and the pinned scanner it compares with this file
fixtures/
  marketplace/             a Claude Code marketplace of three local plugins and eighteen skills (hosted import and CI)
  projects/payments-api/   .mcp.json (hosted MCP import and CI) and .claude/settings.json (CI)
  projects/ops-console/    .vscode/mcp.json, .cursor/mcp.json and a second marketplace with a remote plugin (CI)
  agents/                  eleven A2A agent cards (CI)
```

## The fixtures and the rule ids recorded for them

The rule ids below are what Spellwarden's scan engine 1.4.0, the version the hosted service runs, reported for each fixture when this content was built; they were recorded from the engine's output, not from intentions. Before a snapshot of the demo is taken, the seed check compares the demo organisation's findings with these lines (the skill rows and the two rows of the repository scan); on every push, this repository's Check workflow runs the scanner again and compares its report with every row.

### Skills (hosted import and CI scan)

The demo organisation imports the skills from `https://raw.githubusercontent.com/spellwarden-ai/demo/seed-<n>/fixtures/marketplace/.claude-plugin/marketplace.json`, the marketplace of the seed tag. The hosted import and the CI scan report the same rule ids for each skill. A clean skill has a name, a description, a license, a version and a publisher, and none of the patterns of the other rows.

| Plugin | Skill | What it shows | Rule ids |
|---|---|---|---|
| platform-team | `terraform-plan-checklist` | Clean: license, version, `allowed-hosts`, and the user's confirmation before every destructive command | none |
| platform-team | `kubernetes-rollout-notes` | Clean | none |
| platform-team | `release-notes-writer` | Clean | none |
| platform-team | `cache-cleaner` | A bundled script, committed executable (git mode 100755, which GitHub's archive keeps, so the hosted import sees it too), that removes `$TMPDIR/demo-cache` without asking | SW-SKL-006, SW-SKL-010 |
| platform-team | `quick-installer` | A remote script piped to a shell, from an `.invalid` host; a package installed without a version | SW-SKL-007, SW-SKL-009 |
| platform-team | `agent-config-tuner` | Tells the agent to edit `.claude/settings.json` and to skip the approval prompts | SW-SKL-003, SW-SKL-005 |
| data-team | `warehouse-query-helper` | Clean | none |
| data-team | `csv-profiler` | Clean for the engine; a finding reported by hand in the demo says its output can hold personal data | none |
| data-team | `metrics-dashboard-fetcher` | Reads a web page into the conversation with no list of allowed hosts | SW-SKL-019 |
| data-team | `notebook-runner` | A script line that decodes an encoded command and runs it (it decodes to `echo demo`); a malicious indicator | SW-SKL-004 |
| data-team | `credentials-loader` | Reads the cloud credentials file with no stated purpose; a password written into the skill | SW-SKL-011, SW-SKL-012 |
| data-team | `backup-uploader` | Sends the private SSH key to an outside host (an `.invalid` one); a malicious indicator | SW-SKL-008 |
| support-team | `ticket-summariser` | Clean for the engine; after seeding, the demo organisation's own rule, promoted from a finding reported by hand, fires on it | none |
| support-team | `customer-reply-drafter` | "Ignore previous instructions" and "without telling the user" in its instructions | SW-SKL-001 |
| support-team | `faq-lookup` | A zero-width space inside a word of the FAQ | SW-SKL-002 |
| support-team | `status-page-checker` | The cloud metadata address in a sentence of the instructions | SW-SKL-013 |
| support-team | `log-scrubber` | A 240-character base64 constant in a script (it decodes to `echo demo` lines and nothing reads it) | SW-SKL-014 |
| support-team | `legacy-macro` | A frontmatter block with a name only: no description, license or version | SW-SKL-015, SW-SKL-031 |

### MCP client configuration

`fixtures/projects/payments-api/.mcp.json` is imported by the hosted MCP importer, which probes each HTTPS endpoint once. The endpoints are Spellwarden's demo servers under `https://demo-mcp.spellwarden.ai/<server>/mcp`, each with a fixed behaviour, so each import gives the same migration status and findings:

| Server | Entry | Hosted status | Hosted rule ids |
|---|---|---|---|
| `orders` | `https://demo-mcp.spellwarden.ai/orders/mcp`: current protocol, OAuth with client ID metadata documents | ready | none |
| `tickets` | `https://demo-mcp.spellwarden.ai/tickets/mcp`: the old HTTP and SSE transport | to migrate | SW-MCP-004 |
| `inventory` | `https://demo-mcp.spellwarden.ai/inventory/mcp`: protocol sessions, roots and sampling, no discovery | to migrate | SW-MCP-006, SW-MCP-007, SW-MCP-008 |
| `search` | `https://demo-mcp.spellwarden.ai/search/mcp`: lists its tools without authentication, one with instructions in its description | to migrate | SW-MCP-001, SW-MCP-011 |
| `billing-sandbox` | `https://demo-mcp.spellwarden.ai/billing/mcp` with a static bearer key in a header | to migrate | SW-MCP-002 |
| `analytics` | `https://demo-mcp.spellwarden.ai/analytics/mcp`: dynamic client registration, a resource that does not match | to migrate | SW-MCP-003, SW-MCP-010 |
| `legacy-reports` | `http://demo-mcp.spellwarden.ai/reports/mcp`: plain HTTP, never requested | not probed | SW-MCP-009 |
| `filesystem` | a local server started with `npx`, no version | not probeable | none |
| `crm` | a local server started with `uvx`, pinned, a literal key in its environment; its tools are pasted in at seeding, one with instructions in its description | not probeable | SW-MCP-011 |

The CI scan reads the configuration files without probing them (the workflow does not probe), so it reports configuration rules only:

| File | What it shows | Rule ids (CI scan) |
|---|---|---|
| `fixtures/projects/payments-api/.mcp.json` | A server over plain HTTP, a literal bearer key in a header, a package with no version, a literal value under a secret name | SW-CFG-001, SW-CFG-002, SW-CFG-003, SW-CFG-010 |
| `fixtures/projects/ops-console/.vscode/mcp.json` | A server at a raw IP address (a documentation address) beside a pinned local server | SW-CFG-004 |
| `fixtures/projects/ops-console/.cursor/mcp.json` | The same in Cursor's file | SW-CFG-004 |

### Claude Code settings and marketplace (CI scan)

| File | What it shows | Rule ids (CI scan) |
|---|---|---|
| `fixtures/projects/payments-api/.claude/settings.json` | Approval prompts switched off; a hook that pipes a remote script to a shell; a hook that decodes and runs a payload (`echo demo`); a hook that sends `.env` to an outside host | SW-CFG-005, SW-CFG-006, SW-CFG-007, SW-CFG-008 |
| `fixtures/projects/ops-console/.claude-plugin/marketplace.json` | A plugin from another GitHub repository with no commit pin (the repository it names does not exist) | SW-CFG-009 |

### A2A agent cards (CI scan)

The cards use hosts under `example.com`. No card is fetched from the network: the settings list no remote agents. Ten of the eleven are unsigned, so they also carry the low finding for an unsigned card; signing a card so the scan can verify it needs a published key set, which the demo does not have.

| Card | What it shows | Rule ids (CI scan) |
|---|---|---|
| `fixtures/agents/order-router/.well-known/agent-card.json` | The cleanest card: A2A 1.0, HTTPS, OAuth authorization code with PKCE, scopes per skill; unsigned | SW-A2A-012 |
| `fixtures/agents/billing-assistant/.well-known/agent-card.json` | Its endpoint over plain HTTP on a public host | SW-A2A-004, SW-A2A-012 |
| `fixtures/agents/travel-booker/.well-known/agent-card.json` | The OAuth implicit flow | SW-A2A-005, SW-A2A-012 |
| `fixtures/agents/crm-sync/.well-known/agent-card.json` | OAuth authorization code without PKCE required | SW-A2A-006, SW-A2A-012 |
| `fixtures/agents/public-lookup/.well-known/agent-card.json` | No authentication at all | SW-A2A-007, SW-A2A-012 |
| `fixtures/agents/report-builder/.well-known/agent-card.json` | An API key sent in the URL query | SW-A2A-008, SW-A2A-012 |
| `fixtures/agents/support-triage/.well-known/agent-card.json` | "Ignore previous instructions" in a skill's description | SW-A2A-012, SW-A2A-014 |
| `fixtures/agents/data-export/.well-known/agent-card.json` | A user name and password in its endpoint URL | SW-A2A-012, SW-A2A-015 |
| `fixtures/agents/legacy-router/.well-known/agent.json` | An A2A 0.3 card at the path used before 0.3, with an API key scheme and a requirement | SW-A2A-002, SW-A2A-003, SW-A2A-012 |
| `fixtures/agents/hmac-signer/.well-known/agent-card.json` | Signed with HS256, a shared secret only the agent can check (the signature itself is fake) | SW-A2A-017 |
| `fixtures/agents/twin-fields/.well-known/agent-card.json` | `securitySchemes` and `security_schemes` both present, which readers resolve differently | SW-A2A-012, SW-A2A-019 |

### The scan of the whole repository

The workflow's scan of `main` is the demo's attested default-branch scan. Every run reports the engine's rule ids of every fixture above, CI only and hosted alike. In connected mode, with the demo organisation's registry gate on, a run on `main` also checks every item against the organisation's private registry. The demo organisation's own rules are left out of this record; the seed check compares them separately.

| Scan | Rule ids |
|---|---|
| `repository`: the engine's rules, every run | SW-A2A-002, SW-A2A-003, SW-A2A-004, SW-A2A-005, SW-A2A-006, SW-A2A-007, SW-A2A-008, SW-A2A-012, SW-A2A-014, SW-A2A-015, SW-A2A-017, SW-A2A-019, SW-CFG-001, SW-CFG-002, SW-CFG-003, SW-CFG-004, SW-CFG-005, SW-CFG-006, SW-CFG-007, SW-CFG-008, SW-CFG-009, SW-CFG-010, SW-SKL-001, SW-SKL-002, SW-SKL-003, SW-SKL-004, SW-SKL-005, SW-SKL-006, SW-SKL-007, SW-SKL-008, SW-SKL-009, SW-SKL-010, SW-SKL-011, SW-SKL-012, SW-SKL-013, SW-SKL-014, SW-SKL-015, SW-SKL-019, SW-SKL-031 |
| `repository`: the registry gate, in connected mode on `main` (every item in scope) | SW-REG-001, SW-REG-002, SW-REG-003 |

The registry gate's findings do not depend on which clean items the registry admits:

- SW-REG-001: skills with an open critical or high finding, which the registry never admits (for example the backup uploader and the notebook runner).
- SW-REG-002: the servers of `fixtures/projects/ops-console/`, which the demo organisation never imported, so its registry cannot hold them.
- SW-REG-003: entries the registry cannot judge: the plain HTTP server `legacy-reports`, the unpinned `filesystem` server and the remote plugin with no commit pin.

### The pull request

The branch `demo/payments-retry-skill` adds one skill, payments-retry, which the demo organisation never imported, so its registry does not admit it. The pull request from that branch stays open: its run leaves the Spellwarden comment on the pull request, and its request scan, which judges only what the pull request changes, carries the registry gate's finding SW-REG-001 for the new skill.

### Public servers from the official MCP registry

The demo organisation also holds three to five public servers from the official MCP registry, chosen at seeding and named in [SEED.md](SEED.md). Public servers from the official MCP registry, scanned on the date SEED.md records; their findings are what Spellwarden's checks reported on that date. They were probed once, during seeding, and the demo never contacts them again.

## The workflows

- `.github/workflows/spellwarden.yml` runs the Spellwarden Action (`spellwarden-ai/scan`, pinned to the commit of v1.4.0) on every push to `main`, on pull requests from branches of this repository, and by hand. It uses connected mode into the demo organisation through a CI connection: GitHub's OIDC token, no stored secret. `fail-on: never` keeps the check green while the repository is full of findings on purpose. Pull requests from forks are skipped, and workflow runs of outside contributors need approval.
- `.github/workflows/check.yml` runs `tools/check_repo.py`: at most 2,000 files and 20 MiB, no symbolic links, no names the hosted importer refuses, nothing at the root that Claude Code loads, no provider token shape anywhere, reserved hosts only in the fixtures, the warning on every plugin; then the pinned scanner and a comparison of its report with the rule ids recorded above.

## Seeding

A tag `seed-<n>` marks the content a snapshot of the demo was seeded from; the hosted imports read the files at that tag. [SEED.md](SEED.md) records each seeding.

## Reporting a problem

Write to `hello@spellwarden.ai`. Issues are turned off for this repository.

## License

Apache-2.0, see [LICENSE](LICENSE).
