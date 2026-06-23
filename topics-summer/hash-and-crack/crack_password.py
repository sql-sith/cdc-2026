import hashlib
import itertools
import string
import time

CHARSET = string.ascii_lowercase + string.digits  # must match make_password.py

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

with open("secret_hashes.txt") as f:
    length = int(f.readline().strip())
    target_hash = f.readline().strip()

total_combinations = len(CHARSET) ** length
print(f"Target hash:  {target_hash}")
print(f"Length:       {length}")
print(f"Charset size: {len(CHARSET)}")
print(f"Combinations: {total_combinations:,}")
print("Cracking...")
print()

start = time.time()
attempts = 0
found = None

for candidate_tuple in itertools.product(CHARSET, repeat=length):
    candidate = "".join(candidate_tuple)
    attempts += 1

    if hash_password(candidate) == target_hash:
        found = candidate
        break

    if attempts % 100_000 == 0:
        percent = attempts / total_combinations * 100
        print(f"  ...tried {attempts:,} ({percent:.1f}%)")

elapsed = time.time() - start

if found is not None:
    print()
    print(f"CRACKED! The password is: {found}")
    print(f"Took {attempts:,} attempts in {elapsed:.2f} seconds")
else:
    print()
    print("Did not find the password.")
    print("(Check that CHARSET in this file matches make_password.py.)")
