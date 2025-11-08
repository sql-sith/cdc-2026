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
    <td style="padding: 2px;">Student Cheatsheet</strong></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

# 📝 Using bash (the Bourne-Again Shell)

**Help**

* `cmd --help` will give help for many commands.
* `man cmd` will give very detailed help for most commands. `man` pages can be overwhelming until you get used to reading them.
* `tldr cmd` will give a one-page breakdown of some of the most common ways to use a command. You might have to install this command yourself.

**Filesystem**

* `pwd` → print working directory
* `ls -l` → list files (long format)
* `cd dir` → change directory
* `mkdir dir` → make directory
* `rm file` → remove file
* `rmdir dir` → remove empty directory

**Viewing Files**

* `cat file` → show contents
* `less file` → scroll through file
* `head -n 5 file` → first 5 lines
* `tail -n 5 file` → last 5 lines

**Permissions**

* `ls -l file` → see permissions
* `chmod 600 file` → owner can read/write only

**Searching**

* `grep pattern file` → search text
* `wc -l file` → count lines
* `sort file` → sort lines
* `uniq file` → remove duplicates

**Variables & Scripts**

* `name="Chris"` → set variable
* `echo $name` → print variable
* `if [ condition ]; then ... fi`
* `while [ condition ]; do ... done`
