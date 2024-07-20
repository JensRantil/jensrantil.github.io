#!/bin/bash
set -euo pipefail

# Check all posts have correct file format.
for f in content/posts/*
do
  echo "$f" | grep -Ev '\d{4}-\d{2}-\d{2}_' && (echo "File $f don't start with 'YYYY-MM-dd_'.";exit 1)
done
    
# Check all frontmatter dates match the date in the post filename.
hugo list published | grep content/posts | csvcut -c 1,4 | while IFS= read -r line; do
  IFS=',' read -r file timestamp <<< "$line"
  filedate=$(echo "$file" | grep -Eo '\d{4}-\d{2}-\d{2}')
  timestampdate=$(echo "$timestamp" | grep -Eo '\d{4}-\d{2}-\d{2}')
  if [ "$filedate" != "$timestampdate" ]; then
    echo "Mismatch: $line"
    exit 1
  fi
done
