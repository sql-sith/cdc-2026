# Making Sausage

Given two words, return a new word by combining the first half of the first word with the second half of the second word.

* For odd-length words, the first half is the shorter half.

## Tests

1. `blend_words("yippee", "bagels")` should return `"yipels"`.
2. `blend_words("terra", "cheesie")` should return `"teche"`.
3. `blend_words("tiger", "iguana")` should return `"tiana" (but don't tell Volkswagen)`.
4. `blend_words("pepper", "salt")` should return `"peplt"`.
5. `blend_words("", "")` should return `""`.
6. `blend_words(" ", " ")` should return `""`.
7. What should `blend_words("Aksel Rasmussen", "Skye Kaptin")` return?
