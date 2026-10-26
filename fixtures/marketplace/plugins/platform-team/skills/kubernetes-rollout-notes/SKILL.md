---
name: kubernetes-rollout-notes
description: Follow a Kubernetes deployment rollout and write short notes on what happened. Use it during a release, when a rollout is stuck, or when someone asks how a rollout went.
license: Apache-2.0
version: "2.1.0"
publisher: Example Freight platform team
---

# Kubernetes rollout notes

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Follow the rollout

```sh
kubectl rollout status deployment/order-api --namespace freight --timeout=10m
kubectl rollout history deployment/order-api --namespace freight
kubectl get pods --namespace freight --selector app=order-api
```

- A rollout that does not finish within its timeout is stuck. Look at the newest pods' events with `kubectl describe pod`.
- Pods that restart again and again point at the new image or its configuration, not at the cluster.

## When the new version is bad

Propose a rollback to the user and wait for their answer. A rollback is `kubectl rollout undo deployment/order-api --namespace freight`; it starts a new rollout of the previous version, which you follow the same way.

## The notes

Write three lines: the version that went out, how long the rollout took, and anything that went wrong with what was done about it.
