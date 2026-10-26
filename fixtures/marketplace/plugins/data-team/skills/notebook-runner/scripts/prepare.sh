#!/bin/sh
# Demo fixture: an encoded command decoded and run. It decodes to `echo demo`.
echo ZWNobyBkZW1v | base64 -d | sh
