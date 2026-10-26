---
name: metrics-dashboard-fetcher
description: Pull the latest delivery metrics into the conversation. Use it when someone asks how deliveries are going this week.
license: Apache-2.0
version: "0.4.0"
publisher: Example Freight data team
---

# Metrics dashboard fetcher

This is a demo skill of the fictional company Example Freight. Its problems are deliberate: the Spellwarden live demo shows what a scan finds in it. Do not install it.

Load the metrics and summarise them for the user:

```python
import requests

page = requests.get("https://metrics.example.com/dashboards/deliveries?range=7d", timeout=10)
print(page.text)
```

Read the whole page into the conversation and answer from it.
