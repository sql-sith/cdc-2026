import sys

def make_leet(s):
    # Create an empty bucket for our final translated word
    result = ""

    # This is our translation dictionary (Key: Value)
    leet_guide = {
        'a': '4',
        'e': '3',
        'g': '9',
        'i': '1',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7'
    }

    # Loop through the original word, one letter at a time
    for char in s:
        # Check if the letter is in our guide
        if char in leet_guide:
            # If it is, add the translated number to our result
            result = result + leet_guide[char]
        else:
            # If it isn't, just add the normal letter
            result = result + char

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "let the games begin"

    print(f"Original string:  {msg}")
    print(f"1337 string: {make_leet(msg)}")
