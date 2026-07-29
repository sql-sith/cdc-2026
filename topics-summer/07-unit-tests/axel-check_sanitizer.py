
# Fails (actual output is "#CodingClub" due to title casing)
#assert sanitizer.make_hashtag("coding club") == "codingclub"

# 🚫 NEVER RUNS because line 4 crashed the script!
#assert sanitizer.format_handle("Coder123") == "@coder123"


from sanitizer import make_hashtag, format_handle

def test_hashtag_basic():
    # ❌ FAILS (Logged by pytest, but execution continues)
    assert make_hashtag("coding club") == "codingclub" # Failed!

def test_handle_basic():
    # ✅ STILL RUNS & PASSES!
    assert format_handle("Coder123") == "@coder123"


