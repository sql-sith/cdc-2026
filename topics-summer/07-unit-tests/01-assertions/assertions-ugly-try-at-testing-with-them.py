def add(x, y):
    return x + y

def multiply(x, y):
    return x + y

def do_assert(some_assertion_check):
    # print(some_assertion_check)
    try:
        assert some_assertion_check
        print("PASS:")
        # print(some_assertion_check)
    except Exception as e:
        print("FAIL:")
        # raise(e)
        pass


if __name__ == "__main__":
    print("Beginning assertion tests.")
    do_assert(add(1, 2) == 3)
    do_assert(multiply(1, 2) == 2)
    do_assert(add(10, 10) == 20)
    do_assert(multiply(10, 10) == 100)
    print("Testing completed.")