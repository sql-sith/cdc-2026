<<<<<<< HEAD
from sanitizer import make_hashtag, format_handle

# Fails (actual output is "#CodingClub" due to title casing)
assert make_hashtag("coding club") == "codingclub"

# 🚫 NEVER RUNS because line 4 crashed the script!
assert format_handle("Coder123") == "@coder123"
