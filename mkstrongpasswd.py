import random
import string
import pyperclip

from random_words import RandomWords

print('''
Password Generator 
==================
''')

rw = RandomWords()
count = int(input("How many words should the password contain? "))


# Function to randomly generate a list of random words
def generate_words(count):
    result = []
    for i in range(count):
        result += rw.random_words()
    return result


words = (generate_words(count))


# Function to apply upper and lower case to letters in a random sequence
def random_case(word):
    result = ''
    for char in word:
        case = random.randint(0, 1)
        if case == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


number = random.randint(0, 9)
punctuation = string.punctuation
str_to_list = list(punctuation)
special_character = random.choice(str_to_list)

# Join all items in the list to a string, separated by a separator
passwd = '-'.join(words)

password = passwd + str(number) + special_character
xkcd_password = random_case(password)

print(f"Password generated: {xkcd_password}")
print(f"Password length: {len(password)}")
pyperclip.copy(xkcd_password)
print("Password copied to clipboard.")
