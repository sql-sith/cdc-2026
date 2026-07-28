import re


def test_user_data():
    # what a hack, sorry
    user = {"name": "Naomi", "age": 12, "email": "naomi@dataspacex.com"}
    email_regex = re.compile(r"(?i)\b(?!chris)[A-Z0-9][A-Z0-9._%+-]*@databaseguy.com\b")

    # Evaluate every condition into a list of booleans
    checks = [
        ("Valid age", user["age"] >= 13),
        ("Valid company email", email_regex.search(user["email"])), # find regex
        ("Valid name", len(user["name"]) > 0),
    ]

    # Filter for failures
    failures = [msg for msg, passed in checks if not passed]

    # One single assert at the very end
    assert not failures, f"Failed checks: {failures}"