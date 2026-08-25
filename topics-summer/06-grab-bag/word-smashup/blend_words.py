'''
    1. `blend_words("yippee", "bagels")` should return `"yipels"`.
    2. `blend_words("terra", "cheesie")` should return `"teesie"`.
    3. `blend_words("tiger", "iguana")` should return `"tiana" (but don't tell Volkswagen)`.
    4. `blend_words("pepper", "salt")` should return `"peplt"`.
    5. `blend_words("", "")` should return `""`.
    6. `blend_words(" ", " ")` should return `""`.
    7. What should `blend_words("Aksel Rasmussen", "Skye Kaptin")` return?
'''

def word_pivot(word: str) -> int:
    return len(word)//2

def blend_words(first: str, second: str) -> str:
    first, second = first.strip(), second.strip()
    return first[:word_pivot(first)] + second[word_pivot(second):]

if __name__ == '__main__':
    try:
        if not assert (blend_words("yippee", "bagels") == "xyipels"):
            print("yippee/bagels failed")
        assert (blend_words("terra", "cheesie") == "teesie")
        assert (blend_words("tiger", "iguana") == "tiana")
        assert (blend_words("pepper", "salt") == "peplt")
        assert (blend_words("", "") == "")
        assert (blend_words(" ", " ") == "")
        assert(blend_words("Aksel Rasmussen", "Skye Kaptin") == "Aksel RKaptin")
    except AssertionError as e:
        raise e


