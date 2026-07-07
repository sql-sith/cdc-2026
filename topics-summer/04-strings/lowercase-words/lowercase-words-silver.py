'''
    There are three problems with this code:
        - a naming problem
        - a problem with a function call
        - an obscure performance problem
'''
def get_lowercase_words(s):
    return " ".join([str for str in s.split(" ") if str.lower() == str])


print(get_lowercase_words("I WANT 2 have MOAR happy much joy DOGE DOGE dogE doge mor"))