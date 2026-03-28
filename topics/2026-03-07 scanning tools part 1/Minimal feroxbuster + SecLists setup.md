# 🟦 Minimal feroxbuster + SecLists setup (using `git clone`)

You only need  **two things** :

1. **feroxbuster** (already installed via winget)
2. **A directory containing wordlists** (we’ll clone SecLists manually)

That’s it.

# 🟣 Step 1 — Pick a home for your wordlists

I recommend something predictable and portable:

Code

```
C:\Tools\wordlists
```

Create it:

Code

```
mkdir C:\Tools\wordlists
```

# 🟣 Step 2 — Clone SecLists into that directory

Code

```
cd C:\Tools\wordlists
git clone https://github.com/danielmiessler/SecLists.git
```

This gives you:

Code

```
C:\Tools\wordlists\SecLists\
```

Inside it:

Code

```
Discovery\Web-Content\raft-medium-directories.txt
Discovery\Web-Content\raft-medium-files.txt
...
```

Exactly what feroxbuster expects.

# 🟣 Step 3 — Run feroxbuster with an explicit wordlist

Example:

Code

```
feroxbuster -u http://localhost:3000 ^
  -w C:\Tools\wordlists\SecLists\Discovery\Web-Content\raft-medium-directories.txt
```

This avoids the default `.\SecLists\...` lookup entirely.

# 🟣 Step 4 — (Optional) Add a config file so students don’t need long paths

Feroxbuster supports a config file (your current tab is on the config docs), but here’s the minimal Windows‑friendly version:

Create:

Code

```
%USERPROFILE%\ferox-config.toml
```

Put this inside:

Code

```
wordlist = "C:\\Tools\\wordlists\\SecLists\\Discovery\\Web-Content\\raft-medium-directories.txt"
```

Now students can run:

Code

```
feroxbuster -u http://localhost:3000
```

No flags needed.

# 🟦 One‑shot setup script (Windows PowerShell)

This is the clean, reproducible version you can hand to students:

Code

```
# Create tools directory
New-Item -ItemType Directory -Force -Path "C:\Tools\wordlists" | Out-Null

# Clone SecLists
git clone https://github.com/danielmiessler/SecLists.git C:\Tools\wordlists\SecLists

# Create feroxbuster config
$config = @"
wordlist = "C:\\Tools\\wordlists\\SecLists\\Discovery\\Web-Content\\raft-medium-directories.txt"
"@

$config | Out-File -Encoding ascii "$env:USERPROFILE\ferox-config.toml"

Write-Host "Setup complete. Try: feroxbuster -u http://localhost:3000"
```

This gives you:
