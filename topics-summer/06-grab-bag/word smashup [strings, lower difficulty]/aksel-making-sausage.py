def blend_words(word1: str, word2: str) -> str:
    return (
        word1[:(len(word1)//2)] +
        word2[(len(word2)//2):]
    )

if __name__ == '__main__':
    test_cases = [ # Copied from `README.md`
        ("yippee", "bagels"),
        ("terra", "cheesie"),
        ("tiger", "iguana"),
        ("pepper", "salt"),
        ("", ""),
        (" ", " "),
        ("Aksel Rasmussen", "Skye Kaptin"),
    ]
    out = [ # Copied from `README.md`
        "yipels",
        "teche", # < Bad test case (both first halves)
        "tiana",
        "peplt",
        "",
        "" # < marked as failed, but technically a success since
           #   the spec says nothing about wanting the shorter
           #   second half.
    ] 
    for i, case in enumerate(test_cases):
        a = blend_words(*case)
        print(a)
        if len(out) > i:
            b = out[i]
            print(b, 'success' if b==a else 'failed')
