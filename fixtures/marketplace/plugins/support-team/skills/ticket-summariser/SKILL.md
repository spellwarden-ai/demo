---
name: ticket-summariser
description: Turn a customer email into a support ticket with a short summary. Use it when a customer writes to support about a shipment.
license: Apache-2.0
version: "1.3.0"
publisher: Example Freight support team
---

# Ticket summariser

This is a demo skill of the fictional company Example Freight. Spellwarden's own rules find nothing in it; the demo organisation's own rule, made from a finding someone reported by hand, does.

1. Read the customer's email and find the shipment number, the problem and what the customer asks for.
2. Write a summary of at most three lines: shipment, problem, request.
3. Paste the customer's full email into the ticket below the summary, so the next agent has every detail.
4. Set the priority: high for a missed delivery, normal for everything else.
