import sys

'''
    This version fixes all three issues we noted in the silver version.
'''
def get_lowercase_words(s):
    return " ".join(word for word in s.split() if word == word.lower())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "HELLO world this is A test"

    print(f"Original string:  {msg}")
    print(f"Lower-case words: {get_lowercase_words(msg)}")
