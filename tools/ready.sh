#!/bin/sh
# Slugs that passed a test run made after the latest rule change, have NOTES.md, and aren't deployed.
cd "$(dirname "$0")/.."
CUTOFF="2026-09-27T13:40:00"
for d in demos/*/; do s=$(basename "$d"); r="$d/test-report.json"
  [ -f "$r" ] && [ -f "$d/NOTES.md" ] && { [ ! -f "$d/deploy.json" ] || [ "$r" -nt "$d/deploy.json" ]; } && { [ ! -f "$d/.release-failed" ] || [ "$r" -nt "$d/.release-failed" ]; } && python3 -c "
import json,sys; j=json.load(open('$r')); sys.exit(0 if j['passed'] and j['date']>'$CUTOFF' and any(x['name'].startswith('every pattern appears') for x in j['results']) and any(x['name'].startswith('no monospace') for x in j['results']) else 1)" && echo "$s"
done
