---
name: csv-profiler
description: Profile a CSV file before it is loaded into the warehouse. Use it when someone shares a new export or asks what a file contains.
license: Apache-2.0
version: "1.1.0"
publisher: Example Freight data team
---

# CSV profiler

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Profile the file

```python
import csv
import sys
from collections import Counter

with open(sys.argv[1], newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

print(f"{len(rows)} rows")
for column in rows[0]:
    values = [row[column] for row in rows]
    empty = sum(1 for value in values if not value)
    print(f"{column}: {len(set(values))} distinct, {empty} empty, most common {Counter(values).most_common(1)}")
print(rows[:10])
```

## Report

Give the row count, each column with its distinct and empty counts, and the first ten rows of the file.
