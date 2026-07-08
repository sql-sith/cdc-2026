import sys

def get_lucky_number(name):

    VOWELS='aeiou'
    CONSONANTS='bcdfghjklmnpqrstvwxyz'

    # this is good!
    first_name, second_name = name.casefold().split(" ")

    first_name_length = len(first_name)
    second_name_length = len(second_name)

    # # Original code:
    # first_name_consonants = sum(first_name.count(char) for char in CONSONANTS)

    # # this shows some of the hidden looping but under-counts repeated letters:
    # first_name_consonants = 0
    # for char in CONSONANTS:
    #     if char in first_name:
    #         first_name_consonants += 1

    # this is what python is doing in the quicksilver version, in all its gory:

    ## first name ##
    first_name_consonants = 0
    # The Outer Loop: Iterates 21 times
    for consonant in CONSONANTS:

        # The Inner Loop's .count() functionality (scans entire name)
        for char in first_name:
            if char == consonant:
                first_name_consonants += 1

    ## first name vowels ##
    first_name_vowels = 0
    for vowel in VOWELS:

        # The Inner Loop (what .count() was secretly doing): Scans the whole name
        for char in first_name:
            if char == vowel:
                first_name_vowels += 1

    ## second name consonants ##
    second_name_consonants = 0

    # The Outer Loop: Iterates 21 times
    for consonant in CONSONANTS:

        # The Inner Loop (what .count() was secretly doing): Scans the whole name
        for char in second_name:
            if char == consonant:
                second_name_consonants += 1

    ## second name vowels ##
    second_name_vowels = 0

    # The Outer Loop: Iterates 21 times
    for vowel in VOWELS:

        # The Inner Loop (what .count() was secretly doing): Scans the whole name
        for char in second_name:
            if char == vowel:
                second_name_vowels += 1

    smaller_product = min(first_name_length, second_name_length) \
        * min(first_name_vowels, second_name_vowels) \
        * min(first_name_consonants, second_name_consonants)
    larger_product = max(first_name_length, second_name_length) \
        * max(first_name_vowels, second_name_vowels) \
        * max(first_name_consonants, second_name_consonants)
    diff = larger_product - smaller_product

    return 13 if diff == 0 else diff


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Bubba Gump"

    print(f"The lucky number for {name} is {get_lucky_number(name)}.")
