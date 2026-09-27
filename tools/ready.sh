#!/bin/sh
# Print slugs that passed their tests, have NOTES.md (builder finished) and are not deployed yet.
cd "$(dirname "$0")/.."
for d in demos/*/; do s=$(basename "$d"); r="$d/test-report.json"
  [ -f "$r" ] && [ -f "$d/NOTES.md" ] && [ ! -f "$d/deploy.json" ] && python3 -c "import json,sys;sys.exit(0 if json.load(open('$r'))['passed'] else 1)" && echo "$s"
done
