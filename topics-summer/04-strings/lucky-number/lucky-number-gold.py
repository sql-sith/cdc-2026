import sys

# These are now at the module-level instead of inside a function.
# Frozen sets are hash lookups, not just strings.
# This makes character lookups faster - O(1) instead of O(n) for those who want to know.
VOWELS = frozenset("aeiou")
CONSONANTS = frozenset("bcdfghjklmnpqrstvwxyz")


def _get_name_stats(word: str) -> tuple[int, int, int]:
    """
    Helper function to calculate length, vowel count, and consonant count in a single pass.
    This eliminates the code we wrote twice in the silver-fish version, honoring the DRY
    principle (Don't Repeat Yourself). We've also gone back to loops, getting rid of that
    sneaky performance issue in the silver-fish version.
    """
    vowels = 0
    consonants = 0

    for char in word:
        if char in VOWELS:
            vowels += 1
        elif char in CONSONANTS:
            consonants += 1

    # notice that we can return all three of these at once:
    return len(word), vowels, consonants


def get_lucky_number(name: str) -> int:
    """
    Calculates a lucky number based on the vowel and consonant counts
    of a person's first and last names.
    """
    # Defensive programming: ensure the input is valid before proceeding
    try:
        first_name, last_name = name.casefold().split(" ")
    except ValueError:
        raise ValueError("Input must contain exactly a first and last name separated by a single space.")

    # Unpack the stats using the helper function (DRY principle)
    len1, v1, c1 = _get_name_stats(first_name)
    len2, v2, c2 = _get_name_stats(last_name)

    # Calculate products
    smaller_product = min(len1, len2) * min(v1, v2) * min(c1, c2)
    larger_product = max(len1, len2) * max(v1, v2) * max(c1, c2)

    lucky_number = larger_product - smaller_product

    # Idiomatic Python: returns 13 if lucky_number evaluates to False (i.e., 0)
    return lucky_number or 13


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Bubba Gump"

    print(f"The lucky number for {name} is {get_lucky_number(name)}.")
