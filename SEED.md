# Seed record

Each seeding of the live demo organisation reads this repository at a tag `seed-<n>` and ends with a snapshot that the demo is reset to every night. This file records what each seeding used and captured. The operator fills in each section during the seeding; nothing here is read by a program.

## seed-1

| Field | Value |
|---|---|
| Tag | `seed-1` |
| Commit | _the commit `seed-1` names_ |
| Seeded on (UTC) | _date_ |
| Scan engine | spellwarden 1.4.0 (the hosted service and the Action) |
| Action | `spellwarden-ai/scan` v1.4.0, commit `e698c76727df2739c002a67784adc8b12ecae690` |
| Snapshot | _the snapshot's key and `taken_at`, from `spellwarden-admin demo snapshot`_ |

### Public servers from the official MCP registry

Chosen at seeding, three to five of them, each passed to the seed script as `--registry-server <name>`. A server qualifies when:

1. its registry entry has a public streamable HTTP or SSE remote;
2. it needs no credential to answer the probe's unauthenticated requests;
3. it belongs to a well-known organisation that publishes it for public use; and
4. it gives a migration status different from the other servers chosen.

Each is probed once, during seeding, with at most the probe's nine requests. The demo organisation is never rescanned, so they are not contacted again. The demo labels them as public servers scanned on the date below.

| Registry name | Organisation | Remote (transport and URL) | Migration status | Rule ids | Scanned on |
|---|---|---|---|---|---|
| _name_ | | | | | |
| _name_ | | | | | |
| _name_ | | | | | |

### Counts captured

What `seed.py check` printed before the snapshot.

| Count | Expected | Captured |
|---|---|---|
| demo_skills | 18 | |
| infra_pack_skills | 5 | |
| endpoint_servers | 7 | |
| stdio_servers | 2 | |
| registry_servers | 3 to 5 | |
| memberships_active | 4 | |
| invitations_pending | 1 | |
| eval_runs | 2 | |
| packs | 1 | |
| pack_exports | 2 | |
| org_rules_enabled | 1 | |
| findings_accepted | 1 | |
| findings_superseded | 1 | |
| findings_fixed | 1 | |

### Eval runs

| Run | Tokens used |
|---|---|
| Paired run of `infra-ops-40` on the three clean skills terraform-plan-checklist, kubernetes-rollout-notes and warehouse-query-helper, labelled "Platform skills, October" | |
| Tool-grade run on the `search` demo server | |

### Notes

- The workflow run of the push that put the seed content on `main` fell back to free mode, because the demo organisation had no CI connection yet; that is expected.
- _anything else the operator saw during the seeding_
