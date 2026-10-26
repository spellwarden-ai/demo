#!/bin/sh
# Demo fixture: removes the demo build cache under $TMPDIR without asking first.
rm -rf "$TMPDIR/demo-cache"
echo "demo cache removed"
