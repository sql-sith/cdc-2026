import hashlib
import random
import string

PASSWORD_LENGTH = 4
CHARSET = string.ascii_lowercase + string.digits  # 36 characters: a-z, 0-9

def generate_password(length, charset):
    return "".join(random.choice(charset) for _ in range(length))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = generate_password(PASSWORD_LENGTH, CHARSET)
password_hash = hash_password(password)

with open("secret_hashes.txt", "w") as f:
    f.write(f"{PASSWORD_LENGTH}\n")
    f.write(f"{password_hash}\n")

print(f"Generated password: {password}")
print(f"SHA-256 hash:       {password_hash}")
print(f"Wrote hash + length to secret_hashes.txt")
print()
print("Pretend you never saw the password above.")
print("Now run crack_password.py and let the attacker find it.")
