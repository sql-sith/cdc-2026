import sys

def get_lowercase_words(s):
    result = ""
    current_word = ""

    # We add a sneaky space to the end of the string so our loop
    # knows to check the very last word!
    s = s + " "

    for char in s:
        if char == " ":
            # We hit a space! Time to check the word we've built.
            # 1. Make sure the word isn't empty
            # 2. Check if the word matches its lowercase version
            if current_word != "" and current_word == current_word.lower():

                # Add it to our final result (handling the first word so we don't get a leading space)
                if result == "":
                    result = current_word
                else:
                    result = result + " " + current_word

            # Empty the bucket for the next word
            current_word = ""

        else:
            # Not a space? Keep building the word letter by letter
            current_word = current_word + char

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "HELLO world this is A test"

    print(f"Original string:  {msg}")
    print(f"Lower-case words: {get_lowercase_words(msg)}")
