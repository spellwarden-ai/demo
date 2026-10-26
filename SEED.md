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
