---
name: payments-retry
description: Retry the payment webhooks that failed overnight, one at a time. Use it when the payments dashboard shows failed webhook deliveries.
license: Apache-2.0
version: "0.1.0"
publisher: Example Freight platform team
---

# Payments retry

This is a demo skill of the fictional company Example Freight, added by the demo's open pull request. It is new, so the demo organisation's private registry has not admitted it, and the registry gate reports it on the pull request.

1. List the webhook deliveries that failed since midnight, with their event ids.
2. Show the list to the user and ask which ones to retry.
3. Retry only the deliveries the user chose, one at a time, and report each answer.
4. Leave every other delivery as it is.
