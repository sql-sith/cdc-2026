import sys


def get_lucky_number(name):
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

    # Convert to lowercase and split into a list
    name_parts = name.lower().split(" ")

    # Assign first and second names on separate lines
    first_name = name_parts[0]
    second_name = name_parts[1]

    first_name_length = len(first_name)
    second_name_length = len(second_name)

    # Initialize counters for the first name
    first_name_vowels = 0
    first_name_consonants = 0

    # Loop through the first name to count vowels and consonants
    for char in first_name:
        if char in VOWELS:
            first_name_vowels += 1
        elif char in CONSONANTS:
            first_name_consonants += 1

    # Initialize counters for the second name
    second_name_vowels = 0
    second_name_consonants = 0

    # Loop through the second name to count vowels and consonants
    for char in second_name:
        if char in VOWELS:
            second_name_vowels += 1
        elif char in CONSONANTS:
            second_name_consonants += 1

    # Calculate the smaller and larger products
    smaller_product = (min(first_name_length, second_name_length)
                       * min(first_name_vowels, second_name_vowels)
                       * min(first_name_consonants, second_name_consonants))

    larger_product = (max(first_name_length, second_name_length)
                      * max(first_name_vowels, second_name_vowels)
                      * max(first_name_consonants, second_name_consonants))

    # Calculate the final value
    lucky_number = larger_product - smaller_product

    # Return using an explicit if/else block
    if lucky_number == 0:
        return 13
    else:
        return lucky_number


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Bubba Gump"

    print(f"The lucky number for {name} is {get_lucky_number(name)}.")
