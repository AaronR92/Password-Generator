import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWZYXabcdefghijklmnopqrstuvwxyz1234567890"

def find_len(str):
    counter = 0   
    for _ in str:
        counter += 1
    return counter

def create_password(length: str, contains_dashes: bool):
    password = ""
    for i in range(0, len):
        rand = random.randint(0, find_len(chars)-1)
        password += chars[rand]

        if (contains_dashes == True and i % 2 == 1 and i != len - 1):
            password += '-'

    return password


if __name__ == '__main__':
    len = int(input("Enter the number of letters and numbers of new password: "))
    contains_dashes = bool(input("Should contain dash every 2 symbols? (True/false): "))

    password = create_password(len, contains_dashes)

    print("Your new password is: " + password)
    input("Press 'Enter' to close")
