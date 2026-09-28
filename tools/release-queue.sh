#!/bin/sh
# Release worker. Run up to 3 in parallel. Takes a lock per theme; skips the re-test when the
# builder's passing report is newer than every file in the theme.
cd "$(dirname "$0")/.."
LOG=.cache/release-queue.log
TOTAL=$(grep -cE '^\| [0-9]+ \|' BUILD-STATUS.md)
while :; do
  DONE=$(ls demos/*/deploy.json 2>/dev/null | grep -v _gallery | wc -l | tr -d ' ')
  if [ "$DONE" -ge "$TOTAL" ] && [ -z "$(tools/ready.sh)" ] && [ -f .cache/round2-complete ]; then echo "$(date +%H:%M) all $TOTAL deployed" >> $LOG; exit 0; fi
  NEXT=""
  for s in $(tools/ready.sh); do
    if mkdir "demos/$s/.lock" 2>/dev/null; then NEXT=$s; break; fi
  done
  if [ -z "$NEXT" ]; then sleep 45; continue; fi
  FLAG=""
  NEWER=$(find "themes/$NEXT" "demos/$NEXT/content.json" -type f -newer "demos/$NEXT/test-report.json" ! -name screenshot.png | head -1)
  [ -z "$NEWER" ] && FLAG="--skip-test"
  echo "$(date +%H:%M) releasing $NEXT $FLAG" >> $LOG
  node tools/release.mjs "$NEXT" $FLAG > ".cache/release-$NEXT.log" 2>&1
  if [ -f "demos/$NEXT/deploy.json" ]; then
    echo "$(date +%H:%M) live $NEXT $(python3 -c "import json;print(json.load(open('demos/$NEXT/deploy.json'))['url'])")" >> $LOG
    ( flock_dir=.cache/gallery.lock; while ! mkdir $flock_dir 2>/dev/null; do sleep 5; done
      node tools/make-gallery.mjs >> $LOG 2>&1 && node tools/deploy.mjs _gallery >> $LOG 2>&1
      git add "themes/$NEXT" "demos/$NEXT" "build/$NEXT.py" BUILD-STATUS.md demos/_gallery 2>/dev/null
      git -c user.name="WP-OSS" -c user.email="info@smartner.nl" commit -qm "Add theme: $NEXT

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" >> $LOG 2>&1
      git push -q >> $LOG 2>&1 || echo "$(date +%H:%M) push failed for $NEXT" >> $LOG
      rmdir $flock_dir )
  else
    echo "$(date +%H:%M) FAILED $NEXT (see .cache/release-$NEXT.log)" >> $LOG
    cp "demos/$NEXT/test-report.json" "demos/$NEXT/.release-failed" 2>/dev/null
  fi
  rmdir "demos/$NEXT/.lock" 2>/dev/null
done
