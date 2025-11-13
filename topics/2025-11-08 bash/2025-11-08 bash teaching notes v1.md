<!-- markdownlint-disable MD033 -->

<table style="font-size: 0.85em; line-height: 1.0;">
  <tr>
    <th colspan="2" style="padding: 2px;">Cedar Rapids Area Homeschools Cyber Defense Club</th>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Date</strong></td>
    <td style="padding: 2px;">2025-11-08</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Presenter</strong></td>
    <td style="padding: 2px;">Chris Leonard</td>
  </tr>
  <tr>
    <td style="padding: 2px;"><strong>Document</strong></td>
    <td style="padding: 2px;">Teaching Notes</strong></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

# Using bash (the Bourne-Again Shell)

---

## 🧭 Session Flow (90 minutes)

### 1. **Warm-up & Orientation (10 min)**

* **Goal:** Make sure everyone knows what Bash is and why it matters.
* Quick demo: open a terminal, type `pwd`, `ls`, `whoami`.
* Framing: “This is how you talk directly to your computer—like coding, but immediate.”

---

### 2. **Filesystem Basics (25 min)**

* **Commands:** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `rm`, `rmdir`
* **Mini-challenges:**
  * “Where are you right now?” (`pwd`)
  * “Make a folder called `playground` and go inside it.”
  * “Create a file called `hello.txt` and then delete it.”
  * “Make a folder inside a folder in one command” (`mkdir -p`).
* **Engagement trick:** Run a “race”—who can create a directory tree `school/class/notes` the fastest?

---

### 3. **Looking at Files (15 min)**

* **Commands:** `cat`, `less`, `head`, `tail`
* **Mini-challenges:**
  * “What are the first 5 lines of `/etc/passwd`?”
  * “What’s the last line of that file?”
  * “Why can’t you read `/etc/shadow`?” (teachable moment about permissions).

---

### 4. **Permissions & Ownership (15 min)**

* **Commands:** `ls -l`, `chmod`, `chown`
* **Mini-challenges:**
  * “Who owns `/etc/passwd`?”
  * “What do the `rwx` letters mean?”
  * “Make a file that only you can read.”
* **Optional fun:** Have them try `chmod 000 myfile` and then see what happens when they try to open it.

---

### 5. **Searching & Filtering (15 min)**

* **Commands:** `grep`, `wc`, `sort`, `uniq`
* **Mini-challenges:**
  * “How many users are listed in `/etc/passwd`?” (`wc -l`)
  * “Find all lines with `/bin/bash` in `/etc/passwd`.”
  * “Sort the list of users alphabetically.”

---

### 6. **Intro to Variables & Simple Scripting (10 min, if time)**

* **Concepts:** variables, `if`, `while`
* **Demo only (don’t go too deep):**

  ```bash
  name="Chris"
  echo "Hello, $name"
  ```

  ```bash
  if [ -f /etc/passwd ]; then
    echo "File exists!"
  fi
  ```

  ```bash
  count=1
  while [ $count -le 5 ]; do
    echo "Welcome $count times"
    count=$((count+1))
  done
  ```
* Keep it light—show them the “power” without diving into environment vs. shell variables (too abstract for this level).

---

## 🎯 Teaching Tips

* **Chunk & challenge:** Teach 2–3 commands, then immediately give them a puzzle.
* **Visible progress:** Have them build a “sandbox” directory where they can experiment without fear.
* **Gamify:** Award points for fastest correct solution, or let 12th graders act as “coaches.”
* **Story hooks:** Frame commands as detective work (“Who owns this file?” “What secrets are hidden in this directory?”).

---

## 🚫 What to Skip

* Don’t go deep into  **environment vs. shell variables** —too abstract for beginners.
* Avoid **pipes and redirection** unless you have extra time; they’re powerful but can overwhelm.
* Skip  **ACLs, systemctl, journalctl** —too advanced for this audience.

---
