<!-- markdownlint-disable MD033 -->

# PowerShell Cheatsheet

**Help**

* `cmd --help` will give help for many commands.
* `man cmd` will give very detailed help for most commands. `man` pages can be overwhelming until you get used to reading them.
* `tldr cmd` will give a one-page breakdown of some of the most common ways to use a command. You might have to install this command yourself.

**Filesystem**

* `Get-Location` (aliases: `gci, ls, dir`) → print working directory
* `Get-ChildItem` (aliases: `gci, ls, dir`)→ list files
* `Set-Location` (aliases: `sl, cd, chdir`) → change directory
* `New-Item` (alias: `ni`) → make new file, directory, symbolic link, etc.
* `mkdir ` → helper function to make a new directory
* `Remove-Item` (alias: `ri, rm, rmdir, del, erase, rd`) file → remove file, directory, variable, function, etc.

From this point forward, please look up aliases by typing `help command_name`. the aliases are displayed near the top of each help section.

**Viewing Files**

* `Get-Content` → show contents
* `Get-Content file | more` → scroll through file
* `more file` → alternative way to scroll through file
* `Get-Content -First 5 file` → first 5 lines
* `Get-Content` - `Last 5 file` → last 5 lines

**Permissions**

* `Get-ACL file | Select-Object -ExpandProperty Access # advanced - not everything is simple in PowerShell :)`
* `icacls.exe` → easier, Windows-native way to see file permissions
* `icacls (grant|remove) (user|group) permission` → add or remove permissions. You don't want to do this with Set-ACL until you know you can.

**Searching**

* `Select-String -Pattern pattern -Path file` → search text
* `Get-Content -l file` → count lines
* `Get-Content file | Sort-Object` → sort lines
* `Get-Content file | Sort-Object -Unique `→ remove duplicates

**Variables & Scripts**

* `$name="Chris"` → set variable
* `Write-Host $name` → print variable
* `if (condition) { ... }`
* `foreach [ $var in <list>]; { ... }`
* `command | ForEach-Object { ... }`
* `command | Where-Object { ... }`
