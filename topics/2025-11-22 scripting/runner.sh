#!/bin/bash
# runner.sh

if [[ -z "$1" ]]; then
    MODE="summary"
else
    MODE="$1"
fi

export MODE
echo "Runner: MODE is $MODE"
./child.sh