import getpass
import hashlib
import requests

API_URL = "https://api.pwnedpasswords.com/range/"
HEADERS = {"User-Agent": "cdc-python-class-hibp-demo"}

def sha1_hex(text):
    return hashlib.sha1(text.encode()).hexdigest().upper()

def query_hibp(hash_prefix):
    response = requests.get(API_URL + hash_prefix, headers=HEADERS)
    # automatically checks for error codes and raises errors nicely:
    response.raise_for_status()
    return response.text

def find_suffix(body_text, target_suffix):
    for line in body_text.splitlines():
        line_suffix, line_count = line.split(":")
        if line_suffix == target_suffix:
            return int(line_count)
    return 0

password = getpass.getpass("Enter a password to check: ")

full_hash = sha1_hex(password)
prefix = full_hash[:5]
suffix = full_hash[5:]

print(f"Full SHA-1 hash:               {full_hash}")
print(f"Sent to HIBP (first 5 chars):  {prefix}")
print(f"Kept local (remaining 35):     {suffix}")
print()

response_text = query_hibp(prefix)
returned_count = len(response_text.splitlines())
print(f"HIBP returned {returned_count} candidate hashes starting with {prefix}.")
print()

count = find_suffix(response_text, suffix)

if count == 0:
    print("This password was not found in HIBP's breach database.")
else:
    print(f"This password has been seen in known breaches {count:,} times.")
    print("Do not use it.")
