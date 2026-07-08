import sys

'''
    There are three problems with this code:
        - a naming problem
        - a problem with a function call
        - an obscure performance problem
'''
def get_lowercase_words(s):
    return " ".join([str for str in s.split(" ") if str.lower() == str])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "HELLO world this is A test"

    print(f"Original string:  {msg}")
    print(f"Lower-case words: {get_lowercase_words(msg)}")
