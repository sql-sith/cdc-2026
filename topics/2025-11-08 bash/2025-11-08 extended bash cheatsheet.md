# Extended `bash` cheatsheet

---

## 🔹 Section 1: Core Bash Commands

Here are the most common bash commands, with name explanation if needed and a note about what each one is for. These are all documented in `man bash`.

| Command      | Name Explanation            | Notes                                          |
| ------------ | --------------------------- | ---------------------------------------------- |
| `:`        | *colon* (null command)    | Always succeeds; often used as a placeholder.  |
| `[`        | -                           | Alias for `test`.                            |
| `alias`    | —                          | Define command shortcuts.                      |
| `bg`       | *background*              | Resume a job in the background.                |
| `bind`     | —                          | Bind keyboard sequences to readline functions. |
| `break`    | —                          | Exit from a loop.                              |
| `builtin`  | —                          | Run a shell builtin explicitly.                |
| `cd`       | *change directory*        | Move between directories.                      |
| `command`  | —                          | Run a command, ignoring functions/aliases.     |
| `compgen`  | *completion generator*    | Generate possible completions.                 |
| `complete` | —                          | Specify how arguments are auto-completed.      |
| `continue` | —                          | Resume next iteration of a loop.               |
| `declare`  | —                          | Declare variables and attributes.              |
| `dirs`     | *directories*             | Show directory stack.                          |
| `disown`   | —                          | Remove job from shell’s job table.            |
| `echo`     | —                          | Print arguments to stdout.                     |
| `enable`   | —                          | Enable/disable builtins.                       |
| `eval`     | *evaluate*                | Execute arguments as a command.                |
| `exec`     | *execute*                 | Replace shell with a command.                  |
| `exit`     | —                          | Exit the shell.                                |
| `export`   | —                          | Mark variables for export to environment.      |
| `false`    | —                          | Always returns false.                          |
| `fc`       | *fix command*(from ksh)   | Edit and re-execute commands.                  |
| `fg`       | *foreground*              | Resume a job in the foreground.                |
| `getopts`  | *get options*             | Parse positional parameters.                   |
| `hash`     | —                          | Remember command locations.                    |
| `help`     | —                          | Display help for builtins.                     |
| `history`  | —                          | Show command history.                          |
| `jobs`     | —                          | List active jobs.                              |
| `kill`     | —                          | Send signals to processes.                     |
| `let`      | —                          | Evaluate arithmetic expressions.               |
| `logout`   | —                          | Exit a login shell.                            |
| `popd`     | *pop directory*           | Remove top of directory stack.                 |
| `printf`   | *print formatted*         | Print with formatting.                         |
| `pushd`    | *push directory*          | Add directory to stack.                        |
| `pwd`      | *print working directory* | Show current directory.                        |
| `read`     | —                          | Read input into variables.                     |
| `readonly` | —                          | Mark variables/functions as read-only.         |
| `return`   | —                          | Return from a function.                        |
| `set`      | —                          | Set shell options/variables.                   |
| `shift`    | —                          | Shift positional parameters.                   |
| `shopt`    | *shell options*           | Toggle Bash-specific options.                  |
| `source`   | —                          | Read and execute a file in current shell.      |
| `suspend`  | —                          | Suspend shell execution.                       |
| `test`     | —                          | Evaluate conditional expressions.              |
| `times`    | —                          | Print accumulated user/system times.           |
| `trap`     | —                          | Run commands on signals/events.                |
| `true`     | —                          | Always returns true.                           |
| `type`     | —                          | Show how a command name is interpreted.        |
| `ulimit`   | *user limit*              | Control resource limits.                       |
| `umask`    | *user mask*               | Set default file permissions.                  |
| `unalias`  | —                          | Remove aliases.                                |
| `unset`    | —                          | Remove variables/functions.                    |
| `wait`     | —                          | Wait for jobs to finish.                       |

---

## 🔹 Section 2: Special Builtins (POSIX-defined)

* Bash is POSIX-compliant shell. POSIX is a set of rules to make programs like Bash work consistently across operating systems.
* That standard includes certain requirements for some commands, some of which are listed below.
* These command names are also listed in the Bash Core Commands list above. POSIX behavior says that they must have **special** behavior because they directly affect the shell environment.
* For example, they can **handle errors differently** than other commans: if a POSIX command fails, the shell may exit completely, depending on context.
* These commands are documented in `man bash`.

| Command      | Expansion / Meaning      | Notes                                                                        |
| ------------ | ------------------------ | ---------------------------------------------------------------------------- |
| `:`        | *colon* (null command) | Always succeeds; often used as a placeholder.                                |
| `.`        | *dot* (source)         | Execute commands from a file in the current shell. Equivalent to `source`. |
| `break`    | —                       | Exit from a loop.                                                            |
| `continue` | —                       | Resume next iteration of a loop.                                             |
| `eval`     | *evaluate*             | Execute arguments as a command.                                              |
| `exec`     | *execute*              | Replace shell with a command.                                                |
| `exit`     | —                       | Exit the shell.                                                              |
| `export`   | —                       | Mark variables for export to environment.                                    |
| `readonly` | —                       | Mark variables/functions as read-only.                                       |
| `return`   | —                       | Return from a function.                                                      |
| `set`      | —                       | Set shell options/variables.                                                 |
| `shift`    | —                       | Shift positional parameters.                                                 |
| `times`    | —                       | Print accumulated user/system times.                                         |
| `trap`     | —                       | Run commands on signals/events.                                              |
| `unset`    | —                       | Remove variables/functions.                                                  |

## 🔹 Section 2: Special Bash Reserved Words

These aren’t commands but keywords in the shell grammar:

* `if`, `then`, `else`, `elif`, `fi`
* `case`, `esac`
* `for`, `select`, `while`, `until`, `do`, `done`
* `function`, `{`, `}`
* `[[ … ]]`, `(( … ))`

## 🔹 Section 3: Bash Reserved Words

| Reserved Word | Expansion / Meaning | Notes                                                     |
| ------------- | ------------------- | --------------------------------------------------------- |
| `(( … ))`  | —                  | Arithmetic evaluation.                                    |
| `[[ … ]]`  | —                  | Extended test command (Bash conditional expression).      |
| `{` `}`   | —                  | Group commands.                                           |
| `case`      | —                  | Pattern-matching conditional.                             |
| `coproc`    | *co-process*      | Start a command as a coprocess with its own input/output. |
| `do`        | —                  | Introduces loop body.                                     |
| `done`      | —                  | Ends a loop body.                                         |
| `elif`      | *else if*         | Additional conditional branch.                            |
| `else`      | —                  | Alternative branch if condition fails.                    |
| `esac`      | *end case*        | Ends a `case`block.                                     |
| `fi`        | *finish if*       | Ends an `if`block.                                      |
| `for`       | —                  | Loop over items.                                          |
| `function`  | —                  | Define a function (Bash extension).                       |
| `if`        | —                  | Start a conditional statement.                            |
| `in`        | —                  | Used in `for`loops to specify list.                     |
| `select`    | —                  | Interactive menu loop (unique to Bash/ksh).               |
| `then`      | —                  | Introduces commands to run if condition succeeds.         |
| `time`      | —                  | Measure execution time of a pipeline.                     |
| `until`     | —                  | Loop until condition becomes true.                        |
| `while`     | —                  | Loop while condition is true.                             |

### ✅ Key Takeaway

* Reserved words aren’t commands you invoke like `ls` or `ps`.
* Instead, they’re  **keywords baked into the shell grammar**.
* They control flow, define functions, or mark syntax boundaries. They’re documented in `man bash` and POSIX.
* Reserved words are **syntactic glue** — they don’t expand to longer names. Some (`fi`, `esac`) are mnemonic reversals of their openers.
* Bash adds extras like `select`, `coproc`, and `[[ … ]]` that aren’t in plain POSIX sh.

---

## 🔹 Section 4: External Commands Referenced in Bash

| Command     | Expansion / Meaning         | Notes                                                       |
| ----------- | --------------------------- | ----------------------------------------------------------- |
| `:`       | *colon*(null command)     | Always succeeds; external `true`is similar.               |
| `[`       | *test*(synonym)           | Alias for `test`; requires a closing `]`.               |
| `command` | —                          | Builtin, but also referenced as a utility in POSIX.         |
| `echo`    | —                          | Builtin in Bash, but also external.                         |
| `false`   | —                          | Always returns failure (exit status 1).                     |
| `kill`    | —                          | Builtin in Bash, but also external (`/bin/kill`).         |
| `printf`  | *print formatted*         | Builtin in Bash, but also exists as external utility.       |
| `pwd`     | *print working directory* | Builtin in Bash, but also external (`/bin/pwd`).          |
| `test`    | —                          | Evaluate conditional expressions.                           |
| `true`    | —                          | Always returns success (exit status 0).                     |
| `type`    | —                          | Builtin, but often used to distinguish builtin vs external. |
| `ulimit`  | *user limit*              | Builtin, but conceptually tied to system resource limits.   |

### ✅ Key Takeaway

* Some commands exist **both as builtins and as external binaries** (`echo`, `pwd`, `kill`, `printf`).
* Bash prefers the builtin version unless you explicitly call the external one (e.g., `/bin/echo`).
* `[` is just a quirky alias for `test`, which is ... interesting.

---

## 🔹 Section 5: Commonly Useful External Commands (not already covered)

| Command      | Expansion / Meaning                 | Notes                                                     |
| ------------ | ----------------------------------- | --------------------------------------------------------- |
| `cal`      | *calendar*                        | Display a calendar.                                       |
| `cat`      | *concatenate*                     | Display or join files.                                    |
| `chgrp`    | *change group*                    | Change file group ownership.                              |
| `chmod`    | *change mode*                     | Change file permissions.                                  |
| `chown`    | *change owner*                    | Change file ownership.                                    |
| `clear`    | —                                  | Clear the terminal screen.                                |
| `cmp`      | *compare*                         | Compare files byte by byte.                               |
| `comm`     | *common*                          | Compare two sorted files line by line.                    |
| `cp`       | *copy*                            | Copy files.                                               |
| `curl`     | —                                  | Transfer data with URLs.                                  |
| `cut`      | —                                  | Extract columns/fields from text.                         |
| `date`     | —                                  | Show/set system date/time.                                |
| `df`       | *disk free*                       | Show free/used disk space.                                |
| `diff`     | *difference*                      | Compare files line by line.                               |
| `du`       | *disk usage*                      | Show disk space used by files/directories.                |
| `egrep`    | *extended grep*                   | Grep with extended regex.                                 |
| `fgrep`    | *fixed grep*                      | Grep for fixed strings.                                   |
| `file`     | —                                  | Determine file type.                                      |
| `find`     | —                                  | Search for files in a directory tree.                     |
| `free`     | —                                  | Show memory usage.                                        |
| `grep`     | *global regular expression print* | Search text using regex.                                  |
| `groups`   | —                                  | Show user’s groups.                                      |
| `gunzip`   | —                                  | Decompress gzip files.                                    |
| `gzip`     | *GNU zip*                         | Compress files.                                           |
| `head`     | —                                  | Show first lines of a file.                               |
| `hostname` | —                                  | Show/set system hostname.                                 |
| `htop`     | —                                  | Enhanced process viewer (if installed).                   |
| `id`       | —                                  | Show user identity info.                                  |
| `ifconfig` | *interface config*                | Legacy network interface tool.                            |
| `ip`       | —                                  | Manage network interfaces/routes.                         |
| `killall`  | —                                  | Kill processes by name.                                   |
| `less`     | —                                  | Pager for viewing files interactively.                    |
| `locate`   | —                                  | Find files using a prebuilt index.                        |
| `ls`       | *list*                            | List directory contents.                                  |
| `mkdir`    | *make directory*                  | Create directories.                                       |
| `more`     | —                                  | Older pager, similar to `less`.                         |
| `mount`    | —                                  | Mount filesystems.                                        |
| `mv`       | *move*                            | Move/rename files.                                        |
| `netstat`  | *network statistics*              | Show network connections (deprecated in favor of `ss`). |
| `passwd`   | —                                  | Change user password.                                     |
| `ping`     | —                                  | Test network connectivity.                                |
| `ps`       | *process status*                  | Already covered, but external too.                        |
| `reset`    | —                                  | Reset terminal settings.                                  |
| `rm`       | *remove*                          | Delete files.                                             |
| `rmdir`    | *remove directory*                | Remove empty directories.                                 |
| `scp`      | *secure copy*                     | Copy files over SSH.                                      |
| `sftp`     | *SSH file transfer*               | Transfer files over SSH.                                  |
| `sleep`    | —                                  | Pause for a specified time.                               |
| `sort`     | —                                  | Sort lines of text files.                                 |
| `ss`       | *socket statistics*               | Modern replacement for `netstat`.                       |
| `ssh`      | *secure shell*                    | Remote login/command execution.                           |
| `stat`     | —                                  | Show detailed file status.                                |
| `tail`     | —                                  | Show last lines of a file.                                |
| `tar`      | *tape archive*                    | Archive files.                                            |
| `tee`      | —                                  | Split output to file and stdout.                          |
| `top`      | —                                  | Interactive process viewer.                               |
| `touch`    | —                                  | Create empty file or update timestamps.                   |
| `tr`       | *translate*                       | Translate or delete characters.                           |
| `umask`    | *user mask*                       | Set default file permissions (also builtin).              |
| `umount`   | —                                  | Unmount filesystems.                                      |
| `uname`    | *Unix name*                       | Show system information.                                  |
| `uniq`     | *unique*                          | Filter duplicate lines.                                   |
| `unzip`    | —                                  | Extract zip archives.                                     |
| `uptime`   | —                                  | Show system uptime/load.                                  |
| `w`        | —                                  | Show who is logged in and what they’re doing.            |
| `wc`       | *word count*                      | Count lines, words, characters.                           |
| `wget`     | —                                  | Download files from the web.                              |
| `whereis`  | —                                  | Locate command binaries, sources, and man pages.          |
| `which`    | —                                  | Show path of a command.                                   |
| `who`      | —                                  | Show logged-in users.                                     |
| `xargs`    | —                                  | Build and execute command lines from input.               |
| `yes`      | —                                  | Output a string repeatedly.                               |
| `zcat`     | —                                  | View compressed files.                                    |
| `zip`      | —                                  | Create zip archives.                                      |

### ✅ Key Takeaway

This table captures a generous list of the **most commonly useful external commands** — the ones actually used on a daily basis. If I've missed any, please edit the page.

---

## 🔹 Section 5b: Text Processing & Editors

| Command   | Expansion / Meaning            | Notes                                                                                                                     |
| --------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `awk`   | *Aho, Weinberger, Kernighan* | Pattern‑scanning and text‑processing language. Reads line by line, matches patterns, performs actions.                  |
| `bc`    | *basic calculator*           | Arbitrary precision calculator language. Useful for math in scripts.                                                      |
| `emacs` | —                             | Powerful, extensible editor that you should not use.**Emacs was made by those who are Dead, and the Dead keep it.** |
| `expr`  | *expression evaluator*       | Evaluate expressions (arithmetic, string length, regex match).                                                            |
| `nano`  | —                             | Simple, beginner‑friendly text editor. Easy to use, no modal complexity.                                                 |
| `sed`   | *stream editor*              | Non‑interactive editor for transforming text streams. Often used for substitutions (`sed 's/foo/bar/'`).               |
| `vim`   | *Vi IMproved*                | Advanced text editor for experienced users. Modal editing, scripting, plugins.                                            |

### ✅ Key Takeaway

* **Text processing trio:** `awk`, `sed`, `grep` — the classic Unix pipeline tools.
* **Math helpers:** `bc`, `expr` — lightweight calculators for shell scripts.
* **Editors:** `vim` for power users, `nano` for beginners, and `emacs`… well, for completeness.

---

## 🔹 Section 6: System Administration Commands

| Command         | Expansion / Meaning    | Notes                                                               |
| --------------- | ---------------------- | ------------------------------------------------------------------- |
| `blkid`       | *block ID*           | Show block device attributes (UUID, type).                          |
| `df`          | *disk free*          | Show filesystem disk space usage.                                   |
| `dmesg`       | *diagnostic message* | Print kernel ring buffer messages (boot logs, hardware events).     |
| `du`          | *disk usage*         | Show disk usage of files/directories.                               |
| `free`        | —                     | Show memory usage.                                                  |
| `groups`      | —                     | Show group memberships.                                             |
| `halt`        | —                     | Stop all CPUs; legacy command.                                      |
| `hostnamectl` | *hostname control*   | Manage system hostname and related settings.                        |
| `htop`        | —                     | Enhanced process viewer (if installed).                             |
| `id`          | —                     | Show user identity (UID, GID, groups).                              |
| `init`        | *initialization*     | The first process started by the kernel (historically).             |
| `journalctl`  | *journal control*    | Query and view logs collected by `systemd-journald`.              |
| `kill`        | —                     | Send signals to processes.                                          |
| `killall`     | —                     | Kill processes by name.                                             |
| `last`        | —                     | Show login history from `/var/log/wtmp`.                          |
| `lsblk`       | *list block devices* | Show block devices and their mount points.                          |
| `mount`       | —                     | Mount filesystems.                                                  |
| `passwd`      | —                     | Change user password.                                               |
| `ps`          | *process status*     | Show running processes.                                             |
| `reboot`      | —                     | Restart the system.                                                 |
| `service`     | —                     | Legacy wrapper for SysV init scripts; still used on some systems.   |
| `shutdown`    | —                     | Halt or power off the system safely.                                |
| `su`          | *substitute user*    | Switch user identity (often to root).                               |
| `sudo`        | *superuser do*       | Run commands as another user (commonly root).                       |
| `systemctl`   | *system control*     | Manage `systemd`services and units (start, stop, enable, status). |
| `timedatectl` | *time/date control*  | Manage system clock and time zone.                                  |
| `top`         | —                     | Interactive process viewer.                                         |
| `umount`      | —                     | Unmount filesystems.                                                |
| `uptime`      | —                     | Show how long the system has been running and load averages.        |
| `uptime`      | —                     | Show system uptime and load averages.                               |
| `w`           | —                     | Show logged-in users and their activity.                            |
| `who`         | —                     | Show logged-in users.                                               |

### ✅ Key Takeaway

* **systemd tools (`systemctl`, `journalctl`, `hostnamectl`, `timedatectl`)** are the modern backbone of Linux administration.
* **Legacy tools (`init`, `service`, `halt`)** are still worth knowing for historical context and older systems.
* **Monitoring tools (`dmesg`, `top`, `free`, `uptime`)** give quick insight into system health.
