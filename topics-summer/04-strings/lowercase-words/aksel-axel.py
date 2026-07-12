# lowercase words

# Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word.

UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def get_lowercase_words(start: str):
    start += ' '
    output = ''
    working_word = ''
    for ch in start:
        working_word += ch
        if ch == ' ':
            for char in working_word:
                if char in UPPERCASE_LETTERS:
                    working_word = ''
                    break
            output += working_word
            working_word = ''
    return output[:-1]


if __name__ == "__main__":
    print(get_lowercase_words("hello GOOD world"))
    print("hello world")
    print(get_lowercase_words("these are all lowercase"))
    print("these are all lowercase")
    print(get_lowercase_words("less is NoT more"))
    print("less is more")
    print(get_lowercase_words("DonT eat pizza every OTHER day"))
    print("eat pizza every day")
    print(get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog"))
    print("the quick brown fox jumped over the lazy dog")
