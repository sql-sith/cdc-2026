import hashlib
import itertools
import string
import time

CHARSET = string.ascii_lowercase + string.digits  # must match make_password_simplified.py

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# One for-loop per character position.
# This simplified cracker is hardcoded to passwords of length 4.
def crack(target_hash):
    global CHARSET
    attempts = 0
    for c1 in CHARSET:
        for c2 in CHARSET:
            for c3 in CHARSET:
                for c4 in CHARSET:
                    candidate = c1 + c2 + c3 + c4
                    attempts = attempts + 1
                    if attempts % 100_000 == 0:
                        percent = attempts / total_combinations * 100
                        print(f"  ...tried {attempts:,} ({percent:.1f}%)")
                    if hash_password(candidate) == target_hash:
                        return candidate, attempts

    # # The code above is hard-coded for a specific password length of 4.
    # # The code below can work for any length.

    # global CHARSET
    # global length
    # attempts = 0
    # for candidate_tuple in itertools.product(CHARSET, repeat=length):
    #     candidate = "".join(candidate_tuple)
    #     attempts = attempts + 1
    #     if attempts % 100_000 == 0:
    #         percent = attempts / total_combinations * 100
    #         print(f"  ...tried {attempts:,} ({percent:.1f}%)")
    #     if hash_password(candidate) == target_hash:
    #         return candidate, attempts

    return None, attempts

# Read the hash file
f = open("secret_hashes.txt")
length = int(f.readline().strip())
target_hash = f.readline().strip()
f.close()

# if you switch to the alternative code in crack() that can work with any password
# length, you should remove or comment out this length check:
if length != 4:
    print("This simplified cracker only handles length 4.")
    print("The hash file says the password has length " + str(length) + ".")
    print("Set PASSWORD_LENGTH = 4 in make_password_simplified.py and run it again,")
    print("or use crack_password.py for other lengths.")
else:
    total_combinations = len(CHARSET) ** length
    print("Target hash:  " + target_hash)
    print("Length:       " + str(length))
    print("Charset size: " + str(len(CHARSET)))
    print("Combinations: " + str(total_combinations))
    print("Cracking...")
    print()

start = time.time()
found, attempts = crack(target_hash)
elapsed = time.time() - start

if found is not None:
    print("CRACKED! The password is: " + found)
    print("Took " + str(attempts) + " attempts in " + str(round(elapsed, 2)) + " seconds")
else:
    print("Did not find the password.")
    print("(Check that CHARSET matches make_password_simplified.py.)")
