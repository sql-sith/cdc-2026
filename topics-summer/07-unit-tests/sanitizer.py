# File name: sanitizer.py

def make_hashtag(text):
    """Turns a phrase into a clean hashtag."""
    # Removes spaces, capitalizes words, adds '#'
    words = text.title().split()
    return "#" + "".join(words)

def format_handle(username):
    """Ensures a username starts with @ and is all lowercase."""
    username = username.lower().strip()
    if not username.startswith("@"):
        username = "@" + username
    return username
