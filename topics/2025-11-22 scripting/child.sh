#!/bin/bash
# child.sh

echo "Child sees MODE=$MODE"
if [ "$MODE" = "verbose" ]; then
    echo "Verbose mode: listing current dir"
    ls -la
else
    echo "Summary mode: file counts"
    find . -maxdepth 1 -type f | wc -l
fi
