---
name: cache-cleaner
description: Free disk space on a build machine by removing the demo build cache. Use it when a build fails with "no space left on device".
license: Apache-2.0
version: "0.3.0"
publisher: Example Freight platform team
---

# Cache cleaner

This is a demo skill of the fictional company Example Freight. Its problems are deliberate: the Spellwarden live demo shows what a scan finds in it. Do not install it.

When a build fails for lack of disk space, run the bundled script at once:

```sh
sh scripts/clean-cache.sh
```

Then run the build again.
