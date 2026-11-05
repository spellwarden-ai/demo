---
name: migration-safety-check
description: Check a database migration or data change before it runs on production. Use it when someone asks whether a migration, a backfill or a bulk update is safe to run.
license: Apache-2.0
version: "1.0.0"
publisher: Example Freight data team
---

# Migration safety check

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Before you read the migration

1. Ask which database and which tables it touches, how many rows they hold, and when it is meant to run.
2. Ask how the application is deployed around it: before, after or during the code change that needs it.

## Read the migration

- **Locks.** A change that rewrites or locks a large table blocks the application while it runs. Prefer steps that add first, fill in batches and switch over later.
- **Data loss.** Dropping or narrowing a column, or deleting rows, needs a copy of what is removed and a reason in the change.
- **Order.** Old and new versions of the application both work while the migration runs; a rename is done as add, copy, switch, then drop.
- **Backfills.** A bulk update runs in batches with a limit, can stop and resume, and logs how many rows it changed.
- **Rollback.** There is a tested way back, or the change says why there cannot be one.
- **Checks.** Row counts or a sample comparison prove the result before the old data is removed.

## Report

Say whether the migration is safe to run as written. If it is not, list each change with the reason and the safer order.
