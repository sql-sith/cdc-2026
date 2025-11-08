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
    <td style="padding: 2px;">Student Class Notes</strong></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

# Using bash (the Bourne-Again Shell)

---

# 📚 Bash Lesson Plan

## 0. Setup

* Connect to a Linux computer on ISERink **OR** open a local Linux terminal.
* Create a safe “sandbox” directory to experiment in:

  ```bash
  mkdir ~/bash_playground && cd ~/bash_playground
  ```
* Install and test a utility called `tldr`.

```bash
sudo apt update
sudo apt install tldr
tldr --update
tldr ls
```

> **Note:** unless instructed otherwise, run every command in this worksheet inside your `~/bash_playground` directory.

---

## 1. Orientation

* **Explain:** Bash is a command-line shell—like talking directly to the computer.
* **Commands:** `pwd`, `ls`, `whoami`
* **Mini-challenges:**
  * Where are you in the file system right now?
  * What is your username?

---

## 2. Filesystem Basics

* **Commands:** `pwd`, `ls`, `cd`, `mkdir`, `touch`, `rm`, `rmdir`
* **Mini-challenges:**
  * Create a folder called `school` and inside it make `class/notes`.
  * Make a file called `hello.txt` and delete it.
  * uild `school/class/notes` fastest?

---

## 3. Viewing Files

* **Commands:** `cat`, `less`, `head`, `tail`
* **Mini-challenges:**
  * Show first 5 lines of `/etc/passwd`.
  * Show last line of `/etc/passwd`.
  * Try to read `/etc/shadow` → discuss permissions.

**BONUS!**

* You'll probably want to edit files when you are using a `bash` shell.
* New users tend to prefer using `nano`.
* Create a new file in your `bash_sandbox` directory by using `touch`:

```bash
touch ~/bash_sandbox/test_file.txt
```

* Open the file in `nano`:

```bash
nano ~/bash_sandbox/test_file.txti
```

* Put into the file the names of two nursery rhymes you liked when you were little.
* Now you want to save the file. Look at the bottom of the screen. Nano tells you to type `^O` (`Ctrl-O`) to "write out" the file, which means saving the file. Do this to save your file.
* The other most important action in the `nano` menu is `[^X] Exit`. Type `Ctrl-X` to leave `Nano`.
* After you exit `nano`, use commands we discussed earlier to see what's in the file and then delete the file.

---

## 4. Permissions & Ownership

* **Commands:** `ls -l`, `chmod`
  * Discussion: file modes, or, "what the heck does `-rwxrwxrwx` mean?"
  * `tldr` is your new best friend
* **Mini-challenges:**
  * Who owns `/etc/passwd`?
  * Make a file only you can read (`chmod 600 myfile`).
  * In English, what permissions are given to it by default?
  * Remove all permissions (`chmod 000 myfile`) and try to edit it. What happens?
    * Can you fix this so you can edit the file?

---

## 5. Searching & Filtering

* **Commands:** `grep`, `wc`, `sort`, `uniq`
* **Mini-challenges:**
  * Count users in `/etc/passwd`.
  * Find all users with `/bin/bash`.
  * Sort users alphabetically.

---

## 6. Intro to Variables & Scripting (if time permits)

* **Commands:** variables, `if`, `while`
* **Demo only:**

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
