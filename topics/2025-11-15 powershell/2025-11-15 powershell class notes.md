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

# 📚 Using Windows PowerShell

## 0. Setup

* You can do these exercises on one of my Windows servers on ISEAGE or on your own computer if it is running Windows.
* There are two versions of PowerShell. One has version numbers 5.x and the other has version numbers 7.x.
  * We want to run 7.x. To do this, click the Start button and type `pwsh`. It's critical that you type `pwsh` and not `powershell`.
  * The icon you are looking for is black, not blue.
  * Launch the PowerShell app with the black icon.
  * Type `$PSVersionTable` and hit enter.
    * TAB is still your friend: type `$PSVer{TAB}`
    * Verify that your PSVersion value is 7.x, for example: 7.5.4
* Create a safe sandbox directory to experiment in:

```powershell
New-Item -ItemType Directory -Path $HOME\pwsh_playground -Force
Set-Location $HOME\pwsh_playground
```

> **Note:** unless instructed otherwise, run every command in this worksheet inside your `pwsh_playground` directory.

---

## 1. Orientation

* **Explain:** PowerShell is an object-oriented shell and scripting language that sends .NET objects between commands instead of plain text.
* **cmdlets, commands, and variables:** `Get-Location`, `Get-ChildItem`, `whoami, $env:USER`
* **Mini-challenges:**
  * Where are you in the filesystem right now?
  * What is your username?

---

## 2. Filesystem Basics

* **cmdlets:** `Get-Location`, `Get-ChildItem`, `Set-Location`, `New-Item -ItemType Directory`, `New-Item -ItemType File`, `Remove-Item`
* **Key differences vs bash:** Paths accept both Windows and POSIX styles in PowerShell Core; `Get-ChildItem` lists files and directories and can filter by attributes; `Remove-Item` will remove recursively with `-Recurse -Force`.
* **Mini-challenges:**
  * Create a folder called `school` and inside it make `class\notes`:

```powershell
New-Item -ItemType Directory -Path .\school\class\notes -Force
```

* Make a file called `hello.txt` and delete it:

```powershell
New-Item -ItemType File -Path .\hello.txt -Force
Remove-Item -Path .\hello.txt
```

* Which command is fastest to build `school\class\notes`?Copilot suggests the following. Can you do better?

```powershell
New-Item -ItemType Directory -Path .\school\class\notes -Force
```

> ### **Key differences vs bash**
>
> * PowerShell uses cmdlets with Verb-Noun names
> * PowerShell returns objects not plain text
> * PowerShell has a consistent parameter style (e.g., `-Path`, `-Force`).
> * Pipes pass objects (not plaintext) to "downstream" commands, so those commands can access object properties and methods directly.
>   * You can use `Get-Member` to see this

---

## 3. Viewing Files

* **cmdlets:** `Get-Content`, `more`, `Select-Object -First`, `Select-Object -Last`
* **Key differences vs bash:** `Get-Content` returns each line as a string object; you can pipe it to other cmdlets that accept input objects. Use `-Tail` or `-TotalCount` in newer PowerShell versions for similar behavior to `head`/`tail`.
* **Mini-challenges:**
  * Show first 5 lines of `C:\Windows\System32\drivers\etc\hosts`:

```powershell
Get-Content -Path $env:windir\System32\drivers\etc\hosts -TotalCount 5
```

* Show last line:

```powershell
Get-Content -Path $env:windir\System32\drivers\etc\hosts -Tail 1
```

* Try to read a protected file and discuss permissions. (`Get-Content` will fail if you lack access; show error and explain needing elevated privileges.)

**BONUS!**

* To edit files, a common beginner-friendly editor on Windows is Notepad; on macOS/Linux use `code` or `nano` if installed.
  * We can do better than this.
* Create and open a file:

```powershell
New-Item -Path .\pwsh_sandbox.txt -ItemType File -Force
notepad .\pwsh_sandbox.txt    # Windows
# or
code .\pwsh_sandbox.txt      # VS Code if installed cross-platform
```

* After editing, read the file with `Get-Content`, then remove it with `Remove-Item`.

---

## 4. Permissions and Ownership

* **cmdlets:** `Get-Acl`, `Set-Acl`, `icacls` (Windows), `Get-ChildItem | Get-Acl` to inspect many files
* **Key differences vs bash:** Windows file permissions use ACLs (access control lists) rather than simple rwx bits; PowerShell exposes ACL objects you can inspect and modify. On non-Windows platforms running PowerShell Core, POSIX permissions still apply and `Get-Acl` surfaces them differently.
* **Mini-challenges:**
  * Who owns `C:\Windows\System32\drivers\etc\hosts`? (`Get-Acl` and check `Owner` property)
  * Make a file only readable by you (Windows example using `icacls`):

```powershell
# create file
New-Item -Path .\private.txt -ItemType File -Force

# grant only current user full control and remove others (careful with permissions)
$me = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
icacls .\private.txt /inheritance:r /grant:r "$me:F" /c
```

* In English, what permissions are assigned by default? Examine `Get-Acl` output and explain common default ACL entries.

---

## 5. Searching and Filtering

* **cmdlets:** `Select-String`, `Measure-Object`, `Sort-Object`, `Select-Object`
* **Key differences vs bash:** `Select-String` is the PowerShell equivalent of `grep` but returns MatchInfo objects with useful properties (Line, Filename, Matches). Because cmdlets work with objects, you can filter and sort using properties instead of text processing only.
* **Mini-challenges:**
  * Count lines or matches in a file:

```powershell
Select-String -Path .\example.txt -Pattern '.' | Measure-Object
```

* Find lines containing `bash` in a file:

```powershell
Select-String -Path .\hosts -Pattern 'bash'
```

* Sort a list of users (example using a CSV or Get-LocalUser on Windows):

```powershell
Get-LocalUser | Sort-Object -Property Name
```

---

## 6. Intro to Variables and Scripting

* **cmdlets and constructs:** variables (`$name`), string interpolation, `if`, `foreach`, `while`, functions, script files (`.ps1`)
* **Key differences vs bash:** PowerShell variables are strongly typed by convention (but dynamically typed), begin with `$`, and do not require `export` to be visible to child scopes unless explicitly set. Scripts are `.ps1` files and execution may be restricted by the ExecutionPolicy; you may need to adjust it for running unsigned scripts in learning environments.
* **Security note:** To run scripts you might need to set the policy for your session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

* **Demo examples:**

```powershell
$name = "Chris"
Write-Output "Hello, $name"
```

```powershell
if (Test-Path -Path C:\Windows\System32\drivers\etc\hosts) {
  Write-Output "File exists!"
}
```

```powershell
$count = 1
while ($count -le 5) {
  "Welcome {0} times" -f $count
  $count++
}
```

---

## 7. Objects and the Pipeline

* **Explain:** The pipeline passes objects, not lines of text. You can inspect objects, select properties, and format output.
* **cmdlets:** `Get-Process | Where-Object`, `Get-Service | Select-Object`, `Get-ChildItem | Where-Object { $_.Length -gt 1MB }`
* **Key differences vs bash:** In bash the pipeline passes text streams; in PowerShell each item is a rich object with typed properties and methods accessible via `.` notation. Use `Format-Table` or `Format-List` for display only; avoid formatting cmdlets when further processing is needed.
* **Mini-challenges:**
  * List running processes and find the top memory users:

```powershell
Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 5
```

* Find files larger than 1 MB in your playground:

```powershell
Get-ChildItem -File -Recurse | Where-Object { $_.Length -gt 1MB }
```

---

## 8. Aliases and Cross-Platform Tips

* **Explain:** PowerShell includes many aliases to ease transition (e.g., `ls`, `cat`, `pwd` are aliases to PowerShell cmdlets). Relying on aliases in scripts is discouraged for portability and clarity.
* **Key differences vs bash:** Familiar cmdlets may behave differently because they map to cmdlets returning objects. Scripts intended for cross-platform use should use full cmdlet names (`Get-ChildItem` vs `ls`) and avoid platform-specific paths and features.
* **Mini-challenges:**
  * Show which `ls` maps to what:

```powershell
Get-Alias ls
Get-Command ls
```

* Replace an alias with the full cmdlet in a short script.

---

## 9. Getting Help and Documentation

* **cmdlets:** `Get-Help`, `Get-Help -Examples`, `Get-Help -Full`
* **Key differences vs bash:** PowerShell’s built-in help system is extensive and interactive; `Get-Help <cmdlet>` provides examples and parameter explanations. Update help with `Update-Help`.
* **Mini-challenges:**
  * Show help for `Get-ChildItem` and run an example:

```powershell
Get-Help Get-ChildItem -Examples
```

---

## 10. Putting It Together Lab

* **Task:** Create a small script `class_report.ps1` that:
  * Creates a `school\class\notes` tree if missing.
  * Creates or appends a timestamped note into `notes\log.txt`.
  * Lists the five most recently modified files in `notes`.
* **Starter template:**

```powershell
# class_report.ps1
$root = Join-Path $PWD 'school\class\notes'
New-Item -ItemType Directory -Path $root -Force | Out-Null
$log = Join-Path $root 'log.txt'
"$(Get-Date -Format o) - Quick note about PowerShell" | Out-File -FilePath $log -Append
Get-ChildItem -Path $root -File | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

* **Key differences vs bash:** Use `Join-Path` for safe path construction across platforms; prefer `Out-File` / `Add-Content` for writing rather than redirect operators when you want predictable encoding and object handling.

---

## 11. Next Steps and Resources

* Practice object pipelines: pipe outputs to `Get-Member` to inspect available properties and methods.
* Convert small bash one-liners into PowerShell by replacing text pipelines with object-aware equivalents.
* Experiment with modules from the PowerShell Gallery using `Find-Module` / `Install-Module`.

---

## Quick Reference Summary

* Filesystem: `Get-ChildItem` | Navigation: `Set-Location`, `Get-Location`
* Viewing files: `Get-Content` | Editing: `notepad`, `code`
* Searching: `Select-String` | Counting: `Measure-Object`
* Permissions: `Get-Acl`, `icacls` | Help: `Get-Help`
* Pipeline: pipes pass objects; inspect with `Get-Member`
