# 1337 Speak

Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

| Letter | Leet |
|---|---|
| a | 4     |
| e | 3     |
| g | 9     |
| i | 1     |
| l | 1     |
| o | 0     |
| s | 5     |
| t | 7     |

Characters with no substitution are left unchanged.

Tests:

1. make_leet("cool") should return "c001".
2. make_leet("leet") should return "1337".
3. make_leet("hacker") should return "h4ck3r".
4. make_leet("satellite") should return "547311173".
5. make_leet("abcdefghijklmnopqrstuvwxyz") should return "4bcd3f9h1jk1mn0pqr57uvwxyz".
