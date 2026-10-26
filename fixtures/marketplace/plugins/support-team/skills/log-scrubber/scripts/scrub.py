"""Demo fixture: masks e-mail addresses in a log file. The long constant below is an opaque blob that nothing reads;
it is base64 for ten-character lines of `echo demo`, kept to show what an obfuscated script looks like to a scanner."""
import re
import sys

TABLE = "ZWNobyBkZW1vCmVjaG8gZGVtbwplY2hvIGRlbW8KZWNobyBkZW1vCmVjaG8gZGVtbwplY2hvIGRlbW8KZWNobyBkZW1vCmVjaG8gZGVtbwplY2hvIGRlbW8KZWNobyBkZW1vCmVjaG8gZGVtbwplY2hvIGRlbW8KZWNobyBkZW1vCmVjaG8gZGVtbwplY2hvIGRlbW8KZWNobyBkZW1vCmVjaG8gZGVtbwplY2hvIGRlbW8K"

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

source = sys.argv[1]
with open(source, encoding="utf-8") as handle:
    text = handle.read()
with open(source + ".scrubbed", "w", encoding="utf-8") as handle:
    handle.write(EMAIL.sub("[email removed]", text))
