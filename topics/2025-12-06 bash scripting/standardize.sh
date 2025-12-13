#!/bin/bash
# summarize.sh

for f in *.txt; do
    echo "File: $f"
    cat "$f" | wc -l | awk '{ print "Lines: " $1 }' 
    echo "First four lines:"
    head -n 4 "$f"
    echo "----"
done
