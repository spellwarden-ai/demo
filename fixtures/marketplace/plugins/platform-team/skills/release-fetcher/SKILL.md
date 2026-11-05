---
name: release-fetcher
description: Install the newest build of the team's fleet command line tool. Use it when someone needs the tool on a build agent or a laptop.
license: Apache-2.0
version: "0.4.0"
publisher: Example Freight platform team
allowed-hosts:
  - downloads.example.invalid
---

# Release fetcher

This is a demo skill of the fictional company Example Freight. Its problem is deliberate: the Spellwarden live demo shows what a scan finds in it. Do not install it.

It downloads whatever the latest release is today and runs it, with no checksum or signature check, so a changed release runs unseen. The host is under `.invalid` and never answers.

## Install the tool

```sh
curl -fsSL https://downloads.example.invalid/example-freight/fleet-cli/releases/latest/download/fleet-cli -o fleet-cli
chmod +x fleet-cli
./fleet-cli --version
```

Tell the user which version was installed.
