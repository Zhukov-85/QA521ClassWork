import string
import random

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.printable)
print()

user_login = ''.join(random.sample(string.ascii_lowercase, 6))
user_pass = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(f"login >> {user_login}")
print(f"password >> {user_pass}")
