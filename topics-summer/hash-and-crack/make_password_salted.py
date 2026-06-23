import hashlib
import secrets
import random
import string

PASSWORD_LENGTH = 4
CHARSET = string.ascii_lowercase + string.digits  # 36 characters: a-z, 0-9
SALT_BYTES = 8  # 8 random bytes = 16 hex characters

def generate_password(length, charset):
    # return "".join(random.choice(charset) for _ in range(length))
    return 'ucds'

def generate_salt(num_bytes):
    return secrets.token_hex(num_bytes)

def hash_password(salt, password):
    # Mix the salt in by prepending it to the password before hashing.
    # Real schemes (bcrypt, argon2) mix it in more carefully, but the
    # concept is the same: same password + different salt = different hash.
    return hashlib.sha256((salt + password).encode()).hexdigest()

password = generate_password(PASSWORD_LENGTH, CHARSET)
salt = generate_salt(SALT_BYTES)
password_hash = hash_password(salt, password)

with open("secret_hashes_salted.txt", "w") as f:
    f.write(f"{PASSWORD_LENGTH}\n")
    f.write(f"{salt}\n")
    f.write(f"{password_hash}\n")

print(f"Generated password: {password}")
print(f"Salt (stored next to hash, NOT a secret): {salt}")
print(f"SHA-256(salt + password):                 {password_hash}")
print(f"Wrote length + salt + hash to secret_hashes_salted.txt")
print()
print("Pretend you never saw the password above.")
print("Now run crack_password_salted.py and let the attacker find it.")
