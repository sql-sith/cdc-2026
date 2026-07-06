import hashlib
import random
import string

PASSWORD_LENGTH = 4
CHARSET = string.ascii_lowercase + string.digits  # 36 characters: a-z, 0-9

def generate_password(length, charset):
    password = ""
    for i in range(length):
        password = password + random.choice(charset)
    return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = generate_password(PASSWORD_LENGTH, CHARSET)
password_hash = hash_password(password)

f = open("secret_hashes.txt", "w")
f.write(str(PASSWORD_LENGTH) + "\n")
f.write(password_hash + "\n")
f.close()

print("Generated password: " + password)
print("SHA-256 hash:       " + password_hash)
print("Wrote hash + length to secret_hashes.txt")
print()
print("Pretend you never saw the password above.")
print("Now run crack_password_simplified.py and let the attacker find it.")
