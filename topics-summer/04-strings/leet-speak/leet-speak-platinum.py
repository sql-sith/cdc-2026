import sys

def make_leet(s):
    return s.translate(str.maketrans('aegilost', '43911057'))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "let the games begin"

    print(f"Original string:  {msg}")
    print(f"1337 string: {make_leet(msg)}")
