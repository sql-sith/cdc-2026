import sys

def get_lucky_number(name):

    VOWELS='aeiou'
    CONSONANTS='bcdfghjklmnpqrstvwxyz'

    # this is good!
    first_name, second_name = name.casefold().split(" ")

    # there is an efficiency problem in this paragraph of code:
    first_name_length = len(first_name)
    first_name_consonants = sum(first_name.count(char) for char in CONSONANTS)
    first_name_vowels = sum(first_name.count(char) for char in VOWELS)

    # hey, wait! this code looks awfully familiar...
    second_name_length = len(second_name)
    second_name_consonants = sum(second_name.count(char) for char in CONSONANTS)
    second_name_vowels = sum(second_name.count(char) for char in VOWELS)

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
