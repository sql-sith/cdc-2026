from sanitizer import make_hashtag, format_handle

def test_hashtag_basic():
    # ❌ FAILS (Logged by pytest, but execution continues)
    assert make_hashtag("coding club") == "codingclub"

def test_handle_basic():
    # ✅ STILL RUNS & PASSES!
    assert format_handle("Coder123") == "@coder123"
