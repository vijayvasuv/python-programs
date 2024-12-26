#module to generate random characters
import random
#module to use letters and numbers
import string
import sys

#get user input, handle exception and print results
def main():
    while True:
        try:
            value = input("Enter the length of password: " )
            sys.exit(generate_password(value))
        except ValueError:
            print("Invalid input, please re-try")


#function to generate password
def generate_password(length):
    if length.isnumeric():
#store alphabets and numbers in a string
        character = string.digits + string.ascii_letters
        result = ""
        for _ in range(int(length)):
#use random to generate
            result += random.choice(character)
        return result
#raise exception if input is not a positive number
    else:
        raise ValueError


if __name__ == "__main__":
    main()
