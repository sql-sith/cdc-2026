import sanitizer

# Fails (actual output is "#CodingClub" due to title casing)
assert sanitizer.make_hashtag("coding club") == "codingclub"

# 🚫 NEVER RUNS because line 4 crashed the script!
assert sanitizer.format_handle("Coder123") == "@coder123"
