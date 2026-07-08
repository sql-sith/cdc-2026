import sys

def make_leet(s):
    leet_guide = {'a': '4', 'e': '3', 'g': '9', 'i': '1', 'l': '1', 'o': '0', 's': '5', 't': '7'}

    # .get(char, char) means: "Get the leet value for 'char'. If it doesn't exist, just give me 'char' back."
    return "".join(leet_guide.get(char, char) for char in s)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "let the games begin"

    print(f"Original string:  {msg}")
    print(f"1337 string: {make_leet(msg)}")
