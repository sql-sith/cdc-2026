# Student handout — Bash quick lab (one page)

## Quick setup

* Students copy scripts to their Bash environments
* Make scripts executable then run them:
  ```
  chmod +x runner.sh child.sh
  ./runner.sh
  ```

---

## Script 1 — FOR loop: summarize .txt files

```bash
#!/bin/bash
# summarize.sh

for f in *.txt; do
  echo "File: $f"
  cat "$f" | wc -l | awk '{ print "Lines: " $1 }' 
  echo "First four lines:"
  head -n 4 "$f"
  echo "----"
done
```

Notes immediately after Script 1

* Alternative formatting tools: `sed`, `echo` (with `xargs`), and `printf`.
  * `sed 's/^/Lines: /'`
  * `xargs echo "Lines $1"`
  * `xargs printf "Lines: %s\n"`
* To match multiple extensions: `for f in *.{txt,log,py}; do ...; done`.

---

## Script 2 — if, export, and child script

runner.sh

```bash
#!/usr/bin/env bash
# runner.sh
if [[ -z "$1" ]]; then
  MODE="summary"
else
  MODE="$1"
fi

export MODE
echo "Runner: MODE is $MODE"
./child.sh
```

child.sh

```bash
#!/usr/bin/env bash
# child.sh
echo "Child sees MODE=$MODE"
if [ "$MODE" = "verbose" ]; then
  echo "Verbose mode: listing current dir"
  ls -la
else
  echo "Summary mode: file counts"
  find . -maxdepth 1 -type f | wc -l
fi
```

> Advanced note:
>
> * The code `if [[ -z "$1" ]]; then VAR=default; fi`is equivalent to  `VAR="${1:-default}"`. Present the shorthand after students are comfortable with the longhand.

---

## Two-line cheat-sheet

* FOR loop pattern:

  for x in list; do COMMANDS; done
* IF + export essentials:

  if [ condition ]; then VAR=value; fi; export VAR
