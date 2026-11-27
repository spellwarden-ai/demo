# Seed record

Each seeding of the live demo organisation reads this repository at a tag `seed-<n>` and ends with a snapshot that the demo is reset to every night. This file records what each seeding used and captured. The operator fills in each section during the seeding; nothing here is read by a program.

## seed-1

| Field | Value |
|---|---|
| Tag | `seed-1` |
| Commit | `3869e6242cd6df6d127b855582aa4e3978b2d4fe` |
| Seeded on (UTC) | 2026-10-26 |
| Scan engine | spellwarden 1.4.0 (the hosted service and the Action) |
| Action | `spellwarden-ai/scan` v1.4.0, commit `e698c76727df2739c002a67784adc8b12ecae690` |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261026T214700Z.json.gz`, `taken_at` 2026-10-26T21:47:00Z (535 items, 109 objects) |

### Public servers from the official MCP registry

Chosen at seeding, three to five of them, each passed to the seed script as `--registry-server <name>`. A server qualifies when:

1. its registry entry has a public streamable HTTP or SSE remote;
2. it needs no credential to answer the probe's unauthenticated requests;
3. it belongs to a well-known organisation that publishes it for public use; and
4. it gives a migration status different from the other servers chosen.

Each is probed once, during seeding, with at most the probe's nine requests. The demo organisation is never rescanned, so they are not contacted again. The demo labels them as public servers scanned on the date below.

| Registry name | Organisation | Remote (transport and URL) | Migration status | Rule ids | Scanned on |
|---|---|---|---|---|---|
| `com.microsoft/microsoft-learn-mcp` | Microsoft | streamable HTTP, `https://learn.microsoft.com/api/mcp` | to migrate | SW-MCP-001, SW-MCP-005, SW-MCP-006, SW-MCP-007, SW-MCP-008 | 2026-10-26 |
| `com.cloudflare.mcp/mcp` | Cloudflare | streamable HTTP, `https://docs.mcp.cloudflare.com/mcp` | to migrate | SW-MCP-001, SW-MCP-005, SW-MCP-007 | 2026-10-26 |
| `com.notion/mcp` | Notion | streamable HTTP, `https://mcp.notion.com/mcp` | to migrate | none | 2026-10-26 |
| `app.linear/linear` | Linear | SSE, `https://mcp.linear.app/sse` | to migrate | none | 2026-10-26 |

### Counts captured

What `seed.py check` printed before the snapshot.

| Count | Expected | Captured |
|---|---|---|
| demo_skills | 18 | 18 |
| infra_pack_skills | 5 | 5 |
| endpoint_servers | 7 | 7 |
| stdio_servers | 2 | 2 |
| registry_servers | 3 to 5 | 4 |
| memberships_active | 4 | 4 |
| invitations_pending | 1 | 1 |
| eval_runs | 2 | 2 |
| packs | 1 | 1 |
| pack_exports | 2 | 2 |
| org_rules_enabled | 1 | 1 |
| findings_accepted | 1 | 1 |
| findings_superseded | 1 | 1 |
| findings_fixed | 1 | 1 |

### Eval runs

| Run | Tokens used |
|---|---|
| Paired run of `infra-ops-40` on the three clean skills terraform-plan-checklist, kubernetes-rollout-notes and warehouse-query-helper, labelled "Platform skills, October" | 578,738 for both runs together: agent 124,188 in and 122,690 out, judge 235,952 in and 95,908 out, in 163 model calls (`spellwarden-admin usage evals`, which does not split them by run) |
| Tool-grade run on the `search` demo server | (included above) |

### Notes

- The workflow run of the push that put the seed content on `main` fell back to free mode, because the demo organisation had no CI connection yet; that is expected.
- All four public servers came out "to migrate", so criterion 4 above (a status different from the others) could not be met with the public servers of that date. The Notion and Cloudflare rows are both named `mcp`; their registry names tell them apart.
- Four scans of the import (the skills csv-profiler and iam-least-privilege-review, the servers inventory and billing-sandbox) ended "The scan did not finish": scans that finished in the same second collided on their last write. Each was rescanned alone and passed before `seed.py check`.
- The pull request of step 9 is #1, `demo/payments-retry-skill`, left open.
- The production check of the live demo spec (14.4) passed 11 of 11 after the first reset.

## seed-2

| Field | Value |
|---|---|
| Tag | `seed-2` (annotated, GPG-signed) |
| Commit | `1e06af1` (the pull request branch `demo/payments-retry-skill` merged with it at `5f8056f`) |
| Seeded on (UTC) | 2026-11-05 |
| Scan engine | spellwarden 1.8.1, rules `2026.11.1` (the hosted service and the Action) |
| Action | `spellwarden-ai/scan` v1.8.1, commit `f27614bc85e9418036a2d18173f6e34d7e075b3a` |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261105T191326Z.json.gz` (1,132 items, 385 objects, 4,752,198 bytes) |
| Runtime | the nightly replay (code `docs/specs/2026-11-03-live-demo-seed-2.md`): synthetic traces written by Spellwarden, sent at 02:45 UTC through `https://otel.spellwarden.ai`; the seeding's own replay ran at 18:12 UTC (slot 0, 29 requests, 105 records, 15 sessions, content on) |

### Public servers from the official MCP registry

The same four as seed-1, probed again once during this seeding (every server was rescanned once, seed-2 step 17).

| Registry name | Migration status | Rule ids | Scanned on |
|---|---|---|---|
| `com.microsoft/microsoft-learn-mcp` | to migrate | SW-MCP-001, SW-MCP-005, SW-MCP-006, SW-MCP-007, SW-MCP-008 | 2026-11-05 |
| `com.cloudflare.mcp/mcp` | to migrate | SW-MCP-001, SW-MCP-005, SW-MCP-007 | 2026-11-05 |
| `com.notion/mcp` | to migrate | none | 2026-11-05 |
| `app.linear/linear` | to migrate | none | 2026-11-05 |

### Counts captured

What `seed.py check` printed before the snapshot.

| Count | Expected | Captured |
|---|---|---|
| demo_skills | 23 | 23 |
| infra_pack_skills | 5 | 5 |
| endpoint_servers | 7 | 7 |
| stdio_servers | 2 | 2 |
| registry_servers | 3 to 5 | 4 |
| memberships_active | 4 | 4 |
| invitations_pending | 1 | 1 |
| eval_runs | 6 | 6 |
| packs | 1 | 1 |
| pack_exports | 3 | 3 |
| org_rules_enabled | 1 | 1 |
| findings_accepted | 1 | 1 |
| findings_superseded | 1 | 1 |
| findings_fixed | 1 | 1 |
| allow_entries | 3 | 3 |
| eval_exports | 4, none with content | 4 |
| runtime_sessions | at least 10 a slot | 15 |
| runtime_slots | 1 on the seeding day | 1 |

### Eval runs

The four runs of seed-2, on Amazon Bedrock, with the owner's go; 1,536,972 tokens together.

| Run | Tokens used |
|---|---|
| Session eval run "Support agent sessions, November", 8 sessions sampled | about 18,600 (the platform's month counter, less the three runs below) |
| Paired run of `appsec-40` on `secure-change-review`, "Secure review skill, November" | 441,472 |
| Paired run of `agent-sec-40` on `mcp-config-review`, "MCP review skill, November" | 445,603 |
| Paired run of `data-ops-40` on `migration-safety-check`, "Migration safety skill, November" | 631,291 |

## Engine 1.9.0, 7 November 2026

Not a new seed: the backend moved to engine 1.9.0 (rules `2026.11.2`), which grades `SW-MCP-001` by what the unauthenticated tool list exposes and `SW-MCP-011` by the kind of phrase, and reads a streamed `tools/list` answer whole (it was cut at 4 KiB). The demo organisation was brought onto it without changing its content.

| Field | Value |
|---|---|
| Backend | image `631c46226521` (engine 1.9.0), deployed 2026-11-07 |
| Action | `spellwarden-ai/scan` v1.9.0, commit `f2786a4722eeb550e1af70896c5e6be66af85c8b`; the push of `56fa237` uploaded the default-branch scan by scanner 1.9.0 |
| Rescan | every skill (28) and MCP server (13) once, as Demo developer, all on rules `2026.11.2` |
| Check | `seed.py check` passed |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261107T031753Z.json.gz` (1,329 items, 386 objects, 4,753,252 bytes) |

The four public servers, probed once again during the rescan:

| Registry name | Migration status | Open findings (severity) | Scanned on |
|---|---|---|---|
| `com.microsoft/microsoft-learn-mcp` | to migrate | SW-MCP-001 (medium: three tools, all read-only), SW-MCP-006, SW-MCP-007, SW-MCP-008, SW-MCP-011 (medium: "Always use this tool", steering only), SW-MCP-005 (low) | 2026-11-07 |
| `com.cloudflare.mcp/mcp` | to migrate | SW-MCP-001 (medium: two tools, both read-only), SW-MCP-007, SW-MCP-005 (low) | 2026-11-07 |
| `com.notion/mcp` | to migrate | none | 2026-11-07 |
| `app.linear/linear` | to migrate | none | 2026-11-07 |

Microsoft Learn's three tools were not seen by 1.8.1 (its streamed answer is about 6 KiB), so its `SW-MCP-011` is new; no finding of any fixture or demo server changed. The skill rows and the repository rows of README.md hold on 1.9.0.

## Engine 1.9.1, 7 November 2026

Not a new seed: the backend moved to engine 1.9.1 (rules `2026.11.3`), which tags each rule with the OWASP MCP Top 10 entry it detects (`SW-MCP-011` MCP03, `SW-REG-002` MCP09, MCP04, MCP06 and MCP07 for others; no rule tagged MCP10). Detection and severities are those of 1.9.0, so no finding changed; a finding stores its tags when it is scanned, so the demo organisation was rescanned and snapshotted again to show the new tags.

| Field | Value |
|---|---|
| Backend | image `10f50089ca87` (engine 1.9.1), deployed 2026-11-07 |
| Action | `spellwarden-ai/scan` v1.9.1, commit `7e637381f826a222344aa44816524cd1905e6cc6`; the push of `aee5ae3` uploaded the default-branch scan by scanner 1.9.1 |
| Rescan | every skill (28) and MCP server (13) once, as Demo developer, all on rules `2026.11.3` (`seed.py --from 16`); step 24's replay by hand was not run, the night's replay holds |
| Check | `seed.py check --readme README.md` passed |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261107T161557Z.json.gz` (1,457 items, 386 objects, 4,753,252 bytes) |
| Reset | schedule off for the rescan and on again; `demo reset --dry-run` and one `demo reset`: 20 items put, 1,437 unchanged, nothing deleted; the visitor sees `SW-MCP-011` as MCP03 |

## Engine 1.11.0, 10 November 2026

Not a new seed: the backend moved to engine 1.11.0 (rules `2026.11.4`), which makes `SW-MCP-011`'s patterns precise (whitespace collapsed, the words that make a tool description an instruction; see the engine CHANGELOG). The demo's own servers keep their findings: `search` (`sync_index`, "do not mention it to the user") and `crm` (`sync_contacts`) still give `SW-MCP-011` at high, and every rule id of README.md holds (`tools/check_repo.py --report` on a 1.11.0 scan). A finding stores its rules version when it is scanned, so the demo organisation was rescanned and snapshotted again.

| Field | Value |
|---|---|
| Backend | image `f56677d73211` (engine 1.11.0), deployed 2026-11-10 |
| Action | `spellwarden-ai/scan` v1.11.0, commit `fa56a1f7fea77397d3ed0257223479418aa26153`; the push of `12d09e1` uploaded the default-branch scan by scanner 1.11.0 |
| Rescan | every skill (28) and MCP server (13) once, as Demo developer, all on rules `2026.11.4` (`seed.py --from 16`, then `--from 25`); step 24's replay by hand was not run, the night's replay holds |
| Check | `seed.py check --readme README.md` passed: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 90 runtime sessions in 6 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261110T093838Z.json.gz` (1,585 items, 386 objects, 4,753,252 bytes) |
| Reset | schedule off for the rescan and on again; `demo reset --dry-run` and one `demo reset`: 21 items put, 1,564 unchanged, nothing deleted |

The persona password resets first bounced: for a few minutes that morning the apex MX named Microsoft 365 at priority 0, so the codes went to Microsoft, and SES then suppressed the three persona addresses. They were removed from the account's suppression list once the MX was back to SES at 10 and Microsoft at 20.

## Engine 1.11.1, 10 November 2026

Not a new seed and not a new snapshot: the backend moved to engine 1.11.1 (rules `2026.11.4`, unchanged), which sets TLS 1.2 as the minimum of the CLI's own connections and closes the scanner repository's code scanning alerts. No rule, severity, evidence or fingerprint changed, so the skills and MCP servers were not rescanned.

| Item | Value |
|---|---|
| Backend | image `678ea938f87c` (engine 1.11.1), deployed 2026-11-10 (previous `f56677d73211`) |
| Action | `.github/workflows/spellwarden.yml` pinned to `spellwarden-ai/scan` `b4a6e05` (v1.11.1), commit `3c34629`; its push run uploaded the repository scan by 1.11.1 into DEMO |
| Check | `tools/check_repo.py --report` on a local 1.11.1 scan of this repository: no problems |
| Snapshot | unchanged, `demo-snapshot-6dc89b734bdb798bbd33-20261110T093838Z.json.gz`; the nightly reset puts back the repository's 1.11.0 scan, so the next re-seeding (whose step 16 waits for a scan by the manifest's `scanner_version`, now 1.11.1) needs a push run of this workflow before `seed.py check` |

## Engine 1.12.0, 13 November 2026

Not a new seed: the backend moved to engine 1.12.0 (rules `2026.11.5`), which adds steering and concealment forms to `SW-MCP-011` beside 1.11.1's unchanged patterns (see the engine CHANGELOG). 1.12.0 changes no result here: `search` and `crm` still give `SW-MCP-011` at high and `microsoft-learn-mcp` at medium, as on 1.11.0, and every rule id of README.md holds (`tools/check_repo.py --report` on a 1.12.0 scan). A finding stores its rules version when it is scanned, so the demo organisation was rescanned and snapshotted again.

| Field | Value |
|---|---|
| Backend | image `67afe0dce17f` (engine 1.12.0), deployed 2026-11-13 |
| Action | `spellwarden-ai/scan` v1.12.0, commit `9a593c7512979fdd65b2ecff6f9850f7935f93c0`; the push of `f3bb2e5` uploaded the default-branch scan by scanner 1.12.0 |
| Rescan | every skill (28) and MCP server (13) once, as Demo developer, all on rules `2026.11.5` (`seed.py --from 16`, then `--from 24.2`); step 24's replay by hand was not run, the night's replay holds |
| Check | `seed.py check --readme README.md` passed: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261113T203708Z.json.gz` (1,713 items, 386 objects, 4,753,252 bytes) |
| Reset | schedule off for the rescan and on again; `demo reset --dry-run` and one `demo reset`: 22 items put, 1,691 unchanged, nothing deleted |

## Engine 1.13.0, 14 November 2026

Not a new seed: the backend moved to engine 1.13.0 (rules `2026.11.6`), which adds MITRE ATLAS and OWASP Agentic Skills tags to every finding, renames `SW-MCP-011` to "MCP server text contains instruction-like text", reads a probed server's prompts, resources, templates and instructions, and scans instruction files (`AGENTS.md`, `CLAUDE.md` and the Cursor, Windsurf, Copilot and Gemini files), of which this repository has none (see the engine CHANGELOG). 1.13.0 changes no result here: `search` and `crm` still give `SW-MCP-011` at high and `microsoft-learn-mcp` at medium, every server keeps its status and counts, and every rule id of README.md holds.

| Field | Value |
|---|---|
| Backend | image `edf883238ae4` (engine 1.13.0), deployed 2026-11-14 |
| Action | `spellwarden-ai/scan` v1.13.0, commit `b4718b3698d07cbe1dd6f85a7aab8263a91c2486`; the push of `dac6575` uploaded the default-branch scan by scanner 1.13.0 |
| Rescan | every skill (28) and MCP server (13) once, as Demo developer, all on rules `2026.11.6` (`seed.py --from 16`, then `--from 24.2`); step 24's replay by hand was not run, the night's replay holds |
| Check | `seed.py check --readme README.md` passed: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261114T130833Z.json.gz` (1,830 items, 388 objects, 4,755,296 bytes), made current with `demo use-snapshot` |
| Reset | schedule off for the rescan (with the contract 15 apply) and on again; `demo reset --dry-run` and one `demo reset`: 23 items put, 1,807 unchanged, nothing deleted |

## Engine 1.14.0, 15 November 2026

Not a new seed: the backend moved to engine 1.14.0 (rules `2026.11.6`, unchanged), which adds the machine-wide scan (`spellwarden scan --user`, `--inventory`) and the CycloneDX output format (see the engine CHANGELOG). No rule, severity, evidence or fingerprint changed, so the skills and MCP servers were not rescanned (step 17 skipped). This repository's own CycloneDX export, downloaded from the 1.14.0 workflow run, validates against CycloneDX schema 1.7.2.

| Field | Value |
|---|---|
| Backend | image `88ba75e002f2` (engine 1.14.0), dash `a7d3d8e49269`, deployed 2026-11-15 |
| Action | `spellwarden-ai/scan` v1.14.0, commit `28daf485398b203abab272f44547388734676b37`; the push of `6e71f19` uploaded the default-branch scan by scanner 1.14.0 |
| Replay | `demo replay --dry-run`, then `demo replay` at 03:02 UTC (slot 3: 29 requests, 105 records, 15 sessions), then `seed.py --from 24.2`; steps 25 and 26 were already done and skipped, so no eval run was started |
| Check | `seed.py check --readme README.md` passed before and after the reset: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261115T033454Z.json.gz` (1,831 items, 388 objects, 4,755,296 bytes), made current with `demo use-snapshot` |
| Refusal check | an ingest key "Refusal check" made by Demo owner sent one span to `https://otel.spellwarden.ai/v1/traces` and got `403` "This organisation cannot receive telemetry."; the key was revoked |
| Reset | schedule off for the re-seeding (with the contract 16 apply) and on again; `demo reset --dry-run` and one `demo reset`: 25 items put, 3 deleted, 1,806 unchanged |

## Engine 1.15.0, 15 November 2026

Not a new seed: the backend moved to engine 1.15.0 (rules `2026.11.7`), which adds SW-MCP-012, raised only by the hosted service when a probed MCP server's tools differ from its approved list, the tool list pins of `spellwarden lock --probe` and the ToolHive and Docker MCP Gateway exports (see the engine CHANGELOG). No fixture's rule ids changed: this repository's Check workflow passed on 1.15.0 for `c090e04`. Every skill and MCP server was rescanned once (step 17) so their results carry the new rules version; each probed remote server's first answered probe became its approved tool list, with no finding.

| Field | Value |
|---|---|
| Backend | image `6c3622923017` (engine 1.15.0), dash `ddba0afdd01b`, deployed 2026-11-15 |
| Action | `spellwarden-ai/scan` v1.15.0, commit `3e6b7139389551a1ac7b6a5517a74a8ee07576ff`; the push of `c090e04` uploaded the default-branch scan by scanner 1.15.0 |
| Rescan | `seed.py --from 16`: step 16 saw the scans by 1.15.0, step 17 rescanned every skill and server (rules `2026.11.7`); steps 18 to 23 were already done and skipped |
| Replay | `demo replay --dry-run`, then `demo replay` at 16:22 UTC (105 records, 15 sessions), then `seed.py --from 24.2 --timeout 3000`; steps 25 and 26 were already done and skipped, so no eval run was started |
| Check | `seed.py check --readme README.md` passed before and after the reset: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261115T170222Z.json.gz` (1,955 items, 394 objects, 4,766,340 bytes), the current pointer |
| Refusal check | an ingest key "Refusal check" made by Demo owner sent one span to `https://otel.spellwarden.ai/v1/traces` and got `403` "This organisation cannot receive telemetry."; the key was revoked |
| Reset | schedule off for the re-seeding and on again; `demo reset --dry-run` and one `demo reset`: 26 items put, 3 deleted, 1,929 unchanged; the visitor session answers 200 |
| Replay key | rotated after the snapshot (`7ba968de0cdc`; `7565eeff50c3` revoked) |

## Engine 1.16.0, 16 November 2026

Not a new seed: the backend moved to engine 1.16.0 (rules `2026.11.7`, unchanged), which changes only the machine-wide scan (the workstation upload's outcome in every report, VS Code's user and profile `mcp.json`; see the engine CHANGELOG). No fixture's rule ids changed: this repository's Check workflow passed on 1.16.0 for `f91c7a7`. With the rules version unchanged, step 17 had nothing to rescan.

| Field | Value |
|---|---|
| Backend | image `3261c81b11da` (engine 1.16.0), dash `a0a06a9f3767`, deployed 2026-11-16 |
| Action | `spellwarden-ai/scan` v1.16.0, commit `9f2b0c1c09d36605086814f79a41ab6cf806b8a9`; the push of `f91c7a7` uploaded the default-branch scan by scanner 1.16.0 |
| Rescan | `seed.py --from 16`: step 16 saw the scans by 1.16.0; steps 17 to 23 were already done and skipped |
| Replay | `demo replay --dry-run`, then `demo replay` at 08:41 UTC (slot 4, 105 records, 15 sessions), then `seed.py --from 24.2 --timeout 3000`; steps 25 and 26 were already done and skipped, so no eval run was started |
| Check | `seed.py check --readme README.md` passed before and after the reset: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261116T084239Z.json.gz` (1,958 items, 394 objects, 4,766,340 bytes), the current pointer |
| Refusal check | an ingest key "Refusal check" made by Demo owner sent one span to `https://otel.spellwarden.ai/v1/traces` and got `403` "This organisation cannot receive telemetry."; the key was revoked |
| Reset | schedule off for the re-seeding (with the contract 17 deploy) and on again; `demo reset --dry-run` and one `demo reset`: 29 items put, 3 deleted, 1,929 unchanged; the visitor session answers 200 |
| Replay key | rotated after the snapshot (`2e1ccaf2bbb6`; `7ba968de0cdc` revoked) |

## Engine 1.24.0, 25 November 2026

Not a new seed: the backend moved to engine 1.24.0 (rules `2026.11.9`, 66 rules; from 1.17.0 to 1.24.0 the rules version moved from `2026.11.7`, see the engine CHANGELOG). No fixture's rule ids changed: a local scan by 1.24.0 matched every row of README.md, and this repository's Check workflow passed on 1.24.0 for `2d3202e`. With the rules version changed, step 17 rescanned every skill and server.

| Field | Value |
|---|---|
| Backend | image `51ef18aeda6e` (engine 1.24.0), dash `96b5d8ca4c61`, deployed 2026-11-25 |
| Action | `spellwarden-ai/scan` v1.24.0, commit `b521a08c3a40f589f596df17535c3fb2a4747096`; the push of `2d3202e` uploaded the default-branch scan by scanner 1.24.0 |
| Rescan | `seed.py --from 16`: step 16 saw the scans by 1.24.0; step 17 rescanned the 28 skills and 13 servers (41 requests); steps 18 to 23 were already done and skipped |
| Replay | `demo replay --dry-run`, then `demo replay` at 10:56 UTC, then `seed.py --from 24.2 --timeout 3000`; steps 25 and 26 were already done and skipped, so no eval run was started |
| Check | `seed.py check --readme README.md` passed: 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 4 registry servers |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261125T112732Z.json.gz` (2,084 items, 394 objects, 4,766,340 bytes), the current pointer |
| Refusal check | an ingest key "Refusal check" made by Demo owner sent one span to `https://otel.spellwarden.ai/v1/traces` and got `403` "This organisation cannot receive telemetry."; the key was revoked |
| Reset | schedule off for the re-seeding and on again; the first `demo reset --dry-run` right after the apply answered `snapshot_invalid` (the reset's role policy had just been rewritten), the second passed; one `demo reset`: 32 items put, 3 deleted, 2,052 unchanged; the visitor session answers 200 |
| Replay key | rotated after the snapshot (`2e4230afdc44`; `2e1ccaf2bbb6` revoked) |

## Engine 1.25.0 and the preview of every feature, 27 November 2026

The backend moved to engine 1.25.0 (rules `2026.11.10`, 68 rules), and the demo now shows every page of the left bar to the visitor (code `docs/specs/2026-11-27-demo-all-features.md`). The new fixture `workspaces/notes-desk/.vscode/mcp.json` gives a filesystem server the home directory (SW-CFG-015); README.md records it, and a local scan by 1.25.0 matched every row.

| Field | Value |
|---|---|
| Backend | image `8f112531ec14` (engine 1.25.0, the read exception for the demo's Viewer, the alert sink), dash `32dea600d19e`, deployed 2026-11-27 |
| Action | `spellwarden-ai/scan` v1.25.0, commit `f609334a446e7efb0478e10ae607fa51efaa50c1`; the push of `4f52993` uploaded the default-branch scan by scanner 1.25.0 |
| Rescan | `seed.py --from 16`: step 16 saw the scans by 1.25.0; step 17 rescanned every skill and server; steps 18 to 23 were already done and skipped |
| Replay | `demo replay --dry-run`, then `demo replay` at 13:22 UTC, then `seed.py --from 24.2 --timeout 3000`; steps 25 and 26 were already done and skipped, so no eval run was started |
| Preview (step 27) | two alert destinations to `https://demo-mcp.spellwarden.ai/alert-sink` with a test message each; three export destinations labelled `Sample:`; three workstation inventories from scanner 1.25.0 on the prepared home folders, read whole, with the key "Demo workstation seeding" revoked in the same step; `demo sample-rows` (1 connection, 6 assets, 2 services, 3 destination checks); one catalog skill installed and one collection followed by Demo developer |
| Check | `seed.py check --readme README.md` passed as the owner and as the visitor (seven routes, every audit page): 23 demo skills, 5 Infra Pack skills, 7 endpoint servers, 2 stdio servers, 4 active memberships, 1 pending invitation, 6 eval runs, 1 pack, 3 pack exports, 1 org rule, findings accepted 1, superseded 1, fixed 1, 3 allow entries, 4 eval exports, 105 runtime sessions in 7 slots, 2 alert destinations, 3 export destinations, 3 workstations, 1 DevOps Agent connection, 0 active API keys, 1 catalog install, 1 catalog subscription, 4 registry servers. The first visitor check failed on the last group of the sample Foundry ids, which the account pattern took for an AWS account; the pattern was fixed (code `9f8b200f`, `55b1dffb`) before the check passed |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261127T142101Z.json.gz` (2,257 items, 395 objects, 8,091,161 bytes), the current pointer |
| Refusal check | an ingest key "Refusal check" made by Demo owner sent one span to `https://otel.spellwarden.ai/v1/traces` and got `403` "This organisation cannot receive telemetry."; the key was revoked |
| Reset | schedule off for the re-seeding and on again; `demo reset --dry-run` and one `demo reset`: 43 items put, 3 deleted, 2,214 unchanged; the visitor reads all 13 main and 14 settings pages |
| Replay key | rotated after the snapshot (`474f565156e4`; `2e4230afdc44` revoked) |

## Engine 1.26.0, 27 November 2026

Not a new seed: the backend moved to engine 1.26.0 (rules `2026.11.10`, 68 rules, unchanged from 1.25.0; the release changes only the scanner's Markdown report). No fixture's rule ids changed: a local scan by 1.26.0 matched every row of README.md, and this repository's Check workflow passed on 1.26.0 for `189762f`. With the rules version unchanged, step 17 had nothing to rescan.

| Field | Value |
|---|---|
| Backend | image `4a5cc2594c51` (engine 1.26.0), dash `1b51167ac9ca`, deployed 2026-11-27 |
| Action | `spellwarden-ai/scan` v1.26.0, commit `c75a177e803dce58b9df9f7705e324128b89c5d3`; the push of `189762f` uploaded the default-branch scan by scanner 1.26.0 |
| Reset | schedule off for the re-seeding and on again; `demo reset --dry-run` and one `demo reset`: 46 items put, 0 deleted, 2,217 unchanged; the visitor session answers 200 |
| Rescan | `seed.py --from 16`: step 16 saw the scans by 1.26.0 (2 request scans); steps 18 to 23 were already done and skipped |
| Replay | `demo replay --dry-run`, then `demo replay` at 16:07 UTC (105 records, 15 sessions), then `seed.py --from 24.2 --timeout 3000`: 10 of 8 sessions eligible; steps 25 and 26 were already done and skipped, so no eval run was started |
| Preview | steps 27.1 to 27.7 already done; 27.8 checked the 3 devices again (read whole, nothing outside the fixtures' lists); 27.9 `demo sample-rows` asked for a typed confirmation and was not run, its rows were already there (1 DevOps Agent connection, 3 export destinations) |
| Check | `seed.py check --readme README.md` passed (registry servers 4, catalog installs 1, subscriptions 1, workstations 3, export destinations 3, live API keys 0, among the spec 10.3 counts) |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261127T164012Z.json.gz` (2,263 items, 395 objects, 8,091,161 bytes), the current pointer; the local file was shredded |

## Engine 1.27.0 and seed-3, 27 November 2026

A new tag, `seed-3` (signed, on `d52174e`): the skill `image-thumbnailer` with a stand-in binary, `bin/thumbnail` (64 bytes that start with the ELF magic number, mode 100644, no extension), so the demo keeps an SW-SKL-010 finding. Engine 1.27.0 (rules `2026.11.11`, 68 rules) reports SW-SKL-010 on binary content only: `cache-cleaner`'s executable script is read as a script and no longer reported for being executable, so its row records SW-SKL-006 alone. `seed-1` and `seed-2` were not moved. A local scan by 1.27.0 matched every row of README.md, and this repository's Check workflow passed for `d52174e`.

| Field | Value |
|---|---|
| Backend | image `58fbb3fe3053` (engine 1.27.0), dash `da6b0b8b5b81`, deployed 2026-11-27 |
| Action | `spellwarden-ai/scan` v1.27.0, commit `55c03fb303f5a4248ff318717c900baf4d235c68`; the push of `d52174e` and the merge of main into `demo/payments-retry-skill` (`27f32ef`) uploaded scans by scanner 1.27.0 |
| Reset | schedule off for the re-seeding and on again; `demo reset --dry-run` and one `demo reset`: 63 items put, 4 deleted, 2,351 unchanged |
| Rescan | `seed.py --from 16`: step 16 saw the scans by 1.27.0 (3 request scans); step 17 rescanned every skill and server on `2026.11.11`; 18.3 added `image-thumbnailer` by git source at `seed-3`; the other steps to 23 were already done and skipped |
| Replay | `demo replay --dry-run`, then `demo replay` at 20:43 UTC, then `seed.py --from 24.2 --timeout 3000`: 8 of 8 sessions eligible; steps 25 and 26 were already done and skipped, so no eval run was started |
| Preview | steps 27.1 to 27.7 already done; 27.8 checked the 3 devices again (read whole, nothing outside the fixtures' lists); 27.9 `demo sample-rows --yes` wrote nothing (its rows were there) |
| Check | `seed.py check --readme README.md` passed (24 demo skills, 5 Infra Pack skills); as the visitor, `image-thumbnailer` shows SW-SKL-010 open and `cache-cleaner` SW-SKL-006 open |
| Snapshot | `demo/6dc89b734bdb798bbd33/snapshots/demo-snapshot-6dc89b734bdb798bbd33-20261127T211656Z.json.gz` (2,414 items, 396 objects, 8,174,543 bytes), the current pointer; the local file was shredded |
| Refusal check | an ingest key "Refusal check" made by Demo owner sent one span to `https://otel.spellwarden.ai/v1/traces` and got `403` "This organisation cannot receive telemetry."; the key was revoked |
| Replay key | rotated after the snapshot (`9e5975568ccf`; `474f565156e4` revoked) |
