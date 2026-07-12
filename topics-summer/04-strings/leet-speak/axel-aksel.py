
CONVERSIONS = {
    "a": "4",
    "e": "3",
    "g": "9",
    "i": "1",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7",
}

def make_leet1(start):
    for ch in start:
        if ch == "a":
            start = start.replace("a", "4")
        if ch == "e":
            start = start.replace("e", "3")
        if ch == "g":
            start = start.replace("g", "9")
        if ch == "i":
            start = start.replace("i", "1")
        if ch == "l":
            start = start.replace("l", "1")
        if ch == "o":
            start = start.replace("o", "0")
        if ch == "s":
            start = start.replace("s", "5")
        if ch == "t":
            start = start.replace("t", "7")
    return start


def make_leet2(start):
    for ch in start:
        if ch in CONVERSIONS:
            start = start.replace(ch, CONVERSIONS[ch])
    return start


if __name__ == '__main__':
    print(make_leet1("cool"))
    print("c001")
    print(make_leet1("leet"))
    print("1337")
    print(make_leet1("hacker"))
    print("h4ck3r")
    print(make_leet1("satellite"))
    print("547311173")
    print(make_leet1("abcdefghijklmnopqrstuvwxyz"))
    print("4bcd3f9h1jk1mn0pqr57uvwxyz")

    print(make_leet2("cool"))
    print("c001")
    print(make_leet2("leet"))
    print("1337")
    print(make_leet2("hacker"))
    print("h4ck3r")
    print(make_leet2("satellite"))
    print("547311173")
    print(make_leet2("abcdefghijklmnopqrstuvwxyz"))
    print("4bcd3f9h1jk1mn0pqr57uvwxyz")