Here is the updated, standalone student cheatsheet rebuilt from the ground up around the **Sanitizer Script** example instead of the calculator. It is formatted cleanly without complex code blocks inside table cells so it won't break in your Markdown editor.

---

# Python Unit Testing: Quick-Reference Guide

## 1. The `assert` Statement (Internal Guardrails)

An `assert` statement tests whether a condition is `True`. If it is `True`, Python does nothing and moves to the next line. If it is `False`, Python immediately crashes with an `AssertionError`.

```python
# Syntax: assert <condition>, [optional failure message]
assert 2 + 2 == 4
assert 5 > 10, "5 is definitely not greater than 10!"

```

### ⚠️ Why raw `assert` statements aren't a full test suite

When you put multiple assertions in a standard Python script:

1. **Early Termination:** The **first** assertion that fails halts the entire script. Any checks written below it will never run.
2. **Ignored in Production:** Running Python with the optimize flag (`python -O script.py`) disables all `assert` statements completely.

---

## 2. Testing Frameworks (`pytest`)

`pytest` runs outside your code to test it safely. It searches for files named `test_*.py` and executes every function starting with `test_*()`.

### Raw Script vs. `pytest` Suite

#### ❌ Raw Script (`check_sanitizer.py`)

*Single failure kills the program; later checks never get executed.*

```python
from sanitizer import make_hashtag, format_handle

# Fails (actual output is "#CodingClub" due to title casing)
assert make_hashtag("coding club") == "codingclub"

# 🚫 NEVER RUNS because line 4 crashed the script!
assert format_handle("Coder123") == "@coder123"

```

#### ✅ `pytest` Suite (`test_sanitizer.py`)

*Isolates tests into functions so every test case gets a chance to run.*

```python
from sanitizer import make_hashtag, format_handle

def test_hashtag_basic():
    # ❌ FAILS (Logged by pytest, but execution continues)
    assert make_hashtag("coding club") == "codingclub"

def test_handle_basic():
    # ✅ STILL RUNS & PASSES!
    assert format_handle("Coder123") == "@coder123"

```

---

### Running `pytest` & Terminal Output Examples

To run your tests, open your terminal, navigate to your project folder, and type:

```bash
pytest

```

#### Example 1: Failing Test Output (Sample Output)

When a test fails, `pytest` highlights the error in **RED**, pinpoints the failing file and function name, and shows the exact values that caused the mismatch:

```text
============================= FAILURES =============================
________________________ test_hashtag_basic ________________________

    def test_hashtag_basic():
>       assert make_hashtag("coding club") == "codingclub"
E       AssertionError: assert '#CodingClub' == 'codingclub'
E         - codingclub
E         + #CodingClub

test_sanitizer.py:4: AssertionError
===================== 1 failed, 1 passed in 0.05s =====================

```

#### Example 2: Passing Test Output (Sample Output)

When all tests pass, `pytest` displays a clean green output showing every passing test function:

```text
======================== test session starts ========================
collecting ... items

test_sanitizer.py ..                                          [100%]

========================= 2 passed in 0.02s =========================

```

---

## 3. Testing Complex Objects & Data Structures

When checking JSON payloads or dictionaries with multiple fields, standard assertions stop at the first bad key. Here are the two best ways to get full feedback on all fields:

### Strategy A: Compare the Whole Object (Best for Simple Tests)

Compare your actual data dictionary directly against an expected dictionary. `pytest` will generate a complete **diff** showing *all* mismatched keys in a single view.

```python
actual_user = {"name": "Alex", "age": 12, "email": "bad_email"}
expected_user = {"name": "Alex", "age": 15, "email": "alex@example.com"}

# pytest will highlight both 'age' and 'email' mismatches at once!
assert actual_user == expected_user

```

### Strategy B: Use Subtests (Best for Independent Field Checks)

If you need distinct checks without stopping on the first failure, wrap each `assert` in a `subtests` context block *(requires `pip install pytest-subtests`)*:

```python
def test_user_profile(subtests):
    user = {"name": "Alex", "age": 12, "email": "bad_email"}

    with subtests.test(msg="Check Age"):
        assert user["age"] >= 13        # FAILS! Logs error & continues...

    with subtests.test(msg="Check Email"):
        assert "@" in user["email"]     # FAILS! Logs error & continues...

    with subtests.test(msg="Check Name"):
        assert user["name"] == "Alex"   # PASSES!

```

---

## 💡 Quick Rules of Thumb

* **One scenario per test function:** Keep your `test_*()` functions focused on a single behavior or edge case.
* **Keep assertions simple:** One `assert` per line makes terminal failure reports much easier to read!