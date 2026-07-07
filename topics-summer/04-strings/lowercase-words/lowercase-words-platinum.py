'''
    This version fixes all three issues we noted in the silver version.
'''
def get_lowercase_words_improved(s):
    return " ".join(word for word in s.split() if word == word.lower())

print(get_lowercase_words_improved("hello world gOOd wrld pleaz savvve MEE"))