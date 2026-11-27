import random
import string

characters = string.ascii_letters + string.digits

password = ""

n = int(input("Enter the length of the password>>>"))

for i in range(n):
    password += random.choice(characters)

print(password)
