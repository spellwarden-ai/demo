---
name: warehouse-query-helper
description: Help write and check read-only SQL queries against the shipment warehouse. Use it when someone asks for numbers about shipments, routes or delays.
license: Apache-2.0
version: "1.2.0"
publisher: Example Freight data team
---

# Warehouse query helper

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Write the query

- Queries are read-only: `SELECT` only. A request that needs a change to data goes to the data team instead.
- Name the columns you need; never `SELECT *` on the `shipments` table, which has over a hundred columns.
- Filter on `shipped_on` first: the table is partitioned by that date.

```sql
SELECT route_id, COUNT(*) AS shipments, AVG(delay_minutes) AS average_delay
FROM shipments
WHERE shipped_on >= DATE '2026-10-01' AND shipped_on < DATE '2026-11-01'
GROUP BY route_id
ORDER BY average_delay DESC
LIMIT 20;
```

## Check the answer

Say how many rows the query read and what the filter left out, so the reader can judge the numbers.
