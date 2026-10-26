---
name: terraform-plan-checklist
description: Walk through a Terraform plan before it is applied. Use it when someone asks whether a plan is safe to apply, when a plan replaces or destroys resources, or before any destroy.
license: Apache-2.0
version: "1.4.0"
publisher: Example Freight platform team
allowed-hosts:
  - docs.example.com
---

# Terraform plan checklist

This is a demo skill of the fictional company Example Freight. It is one of the clean skills of the Spellwarden live demo.

## Before you read the plan

1. Ask which workspace and which change the plan is for, and write both down.
2. Run `terraform plan -out=change.tfplan` and keep the file; review that file, not a new plan.
3. Read the team's conventions at https://docs.example.com/terraform when a naming or tagging question comes up.

## Read the plan

- Count the creates, changes, replacements and destroys, and compare them with the change.
- A replacement (`-/+`) of a database, a volume or a bucket loses data unless the change says why it is safe.
- A change nobody can explain blocks the apply until someone does.

## Destructive commands

Every destructive command waits for the user to confirm it, in the same session, after they have seen the plan.

```sh
# Show the plan, then ask the user to type yes before anything is destroyed.
terraform show change.tfplan
read -r -p "Apply this plan to workspace $(terraform workspace show)? Type yes to confirm: " answer
[ "$answer" = "yes" ] && terraform apply change.tfplan
```

```sh
# Destroy only after the user has confirmed the workspace by name.
read -r -p "Destroy every resource in workspace $(terraform workspace show)? Type the workspace name to confirm: " answer
[ "$answer" = "$(terraform workspace show)" ] && terraform destroy
```

## After the apply

Write a two-line summary: what changed, and where the plan file is kept.
