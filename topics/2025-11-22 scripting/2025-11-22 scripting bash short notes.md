### Student handout — Bash quick lab (one page)

#### Quick setup

* Make scripts executable then run them:

  chmod +x runner.sh child.sh

  ./runner.sh

---

#### Script 1 — FOR loop: summarize .txt files

```bash
#!/usr/bin/env bash
for f in *.txt; do
  echo "File: $f"
  cat "$f" | wc -l | sed 's/^/Lines: /'
  echo "First four lines:"
  head -n 4 "$f"
  echo "----"
done
```

Notes immediately after Script 1

* Alternative formatting tools: `awk`, `printf`, and `echo` itself.
* To match multiple extensions: `for f in *.{txt,log,py}; do ...; done`.

---

#### Script 2 — IF, export, and child script (longhand default)

runner.sh

```bash
#!/usr/bin/env bash
# runner.sh - longhand default assignment
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

Teaching note for instructor

* The explicit longhand default (`if [[ -z "$1" ]]; then VAR=default; fi`) is equivalent to the shorthand `VAR="${1:-default}"`. Present the shorthand after students are comfortable with the longhand.

---

#### Two-line cheat-sheet (copy on your terminal)

* FOR loop pattern:

  for x in list; do COMMANDS; done
* IF + export essentials:

  if [ condition ]; then VAR=value; fi; export VAR
