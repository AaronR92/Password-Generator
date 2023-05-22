import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWZYXabcdefghijklmnopqrstuvwxyz1234567890"

len = int(input("Enter the length of new password: "))
password = ""

def findLen(str):
    counter = 0   
    for i in str:
        counter += 1
    return counter

for i in range(0, len):
    rand = random.randint(0, findLen(chars)-1)
    password += chars[rand]

print("Your new password is: " + password)

input("Press 'Enter' to close")