### Instructor Guide — Bash Scripting: 1‑Hour Lesson

---

### Overview and goals

* Purpose: teach beginners how to use bash as a scripting language by alternating short interactive reviews with practical scripting exercises.
* Outcomes: students will be able to run simple for loops, use if/then branching, set a default parameter longhand, and understand how export passes values to child processes.
* Audience: green students with some exposure to the shell (ls, cat, grep) but new to structured scripting.

---

### Timing and flow (60 minutes)

* 0–5 min — Welcome, goals, and quick safety/etiquette (don’t run unknown scripts).
* 5–15 min — REVIEW 1: quick interactive recap of three core commands.
* 15–30 min — SCRIPT 1: FOR loop that summarizes .txt files (guided typing + run).
* 30–40 min — REVIEW 2: three additional basic commands (head/tail, wc, chmod).
* 40–55 min — SCRIPT 2: IF / export / child script with explicit longhand default (guided).
* 55–60 min — Wrap, quick recap, homework suggestions, pointers to the repo.

---

### Review 1 — core commands (5–10 minutes)

Goal: warm the class with familiar, one-line commands. Keep each demo short and invite a volunteer to run one.

* ls — show directory contents; demo: ls -la
* cat — show file contents; demo: cat file.txt; cat file1 file2
* grep — search inside files; demo: grep 'TODO' *.md; mention -i for case-insensitive

Teaching prompt: ask one student to run command --help or man to find one flag to show the class.

---

### Script 1 — FOR loop: summarize .txt files (15 minutes)

Goal: demonstrate how a for loop automates repeating the same commands for many files. Have students type and run this script.

Starter script (type, save, run):

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

Walkthrough highlights

* `for f in *.txt` expands to each .txt file in the current directory.
* Quote `"$f"` to handle filenames with spaces.
* `cat "$f" | wc -l | sed 's/^/Lines: /'` prints the number of lines prefixed with "Lines: ".
* `head -n 4` shows the first four lines as a quick sample.

Notes immediately after Script 1

* Alternative formatting tools: `awk`, `printf`, and `echo` itself.
* To match multiple extensions use brace expansion: `for f in *.{txt,log,py}; do ...; done`.

Class activity

* Have 2–3 students modify the loop to append results to summary.txt with `>>` and run it. Verify summary.txt content together.

Instructor debugging tip

* If a student gets no output, ask them to `ls -la` to confirm .txt files exist in the current working directory.

---

### Review 2 — three additional basic commands (10 minutes)

Goal: prepare students for the branching and child-process examples.

* head/tail — demo `head -n 4 file.txt` and `tail -n 5 file.log`.
* wc — demo `wc -l file.txt` and `wc -w file.txt`.
* chmod — demo `chmod +x script.sh` then `./script.sh`.

Teaching prompt: run a quick exercise where a volunteer makes a tiny script executable and runs it.

---

### Script 2 — IF, export, and child script (15 minutes)

Goal: introduce branching with a readable longhand default assignment, demonstrate export inheritance, and practice running a child script.

Practical export explanation to read aloud

* "If you export a variable, processes you start from this shell get a copy of that name/value; non-exported variables stay only in this shell."

Example files (type, save, make executable)
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

Demonstration steps

1. chmod +x runner.sh child.sh
2. Run ./runner.sh to show default ("summary") behavior.
3. Run ./runner.sh verbose to show the verbose branch.
4. Show the effect of removing export MODE (or set MODE without export) and re-run to demonstrate child no longer sees the value.
5. Quick subshell demo: `MODE=foo bash -c 'echo subshell MODE=$MODE'` to illustrate how exported values propagate to subprocesses started from the shell.

Class activity

* Students edit runner.sh to change the default to a different word (e.g., detailed) and run different cases.

Teaching note for instructor (explicit)

* Use the longhand default: `if [[ -z "$1" ]]; then VAR=default; fi` for clarity with beginners. After students are comfortable, show the shorthand `VAR="${1:-default}"` and explain it does the same thing more tersely.

---

### Wrap-up, extensions, and homework (5 minutes)

Quick recap

* FOR automates repetition; IF chooses execution path; export shares variables with child processes.

Short extensions / homework

* Add a timestamp header to the summary file produced by Script 1.
* Modify child.sh to write logs into a logs/ directory and rotate old logs by moving them into an archive directory with a date suffix.
* Optional advanced for strong students: replace the simple glob with a null-safe find/read loop: `while IFS= read -r -d '' file; do ...; done < <(find . -name '*.txt' -print0)`.

Instructor reminders

* Always quote variables (`"$var"`) to avoid word splitting and filename issues.
* Use `set -x` briefly to show students command expansions when debugging; turn off with `set +x`.
* Prepare a small set of sample .txt files in the repo so demonstrations are deterministic for everyone.

---

### Materials to distribute

* Student Lab Sheet (one-page handout you approved) — contains Script 1, Script 2, shortened notes, and the two-line cheat sheet.
* Instructor copy (this guide) with timing, prompts, and troubleshooting notes.

If you want, I can produce a printable PDF version of the Instructor Guide formatted for a single sheet (two sides) and a matching one-page student handout ready for printing.
