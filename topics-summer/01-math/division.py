def divide(numerator, denominator, precision):
    # Newton's method: each pass gets us closer to 1/denominator.
    # The update rule:  new_guess = guess * (2 - denominator * guess)

    guess = .000001                    # any tiny positive number works
    tolerance = 10 ** (-precision)

    while True:
        new_guess = guess * (2 - denominator * guess)
        if abs(new_guess - guess) < tolerance:
            break
        guess = new_guess

    return round(numerator * new_guess, precision)

print(divide (22, 7, 100000))