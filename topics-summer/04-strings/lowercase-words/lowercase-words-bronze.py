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


print(get_lowercase_words("HELLO world this is A test"))
# Output: world this is test
