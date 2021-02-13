import secrets
import random
import string
import pyperclip

# Program that generates random words from a .txt file

print('''
Password Generator 
==================
''')

with open(r"C:\Users\Shadow\Desktop\words_dictionary.txt", "r") as file:
    all_text = file.read()
    words = list(map(str, all_text.split()))

while True:
    try:
        count = int(input("How many words should the password contain? "))
    except ValueError:
        print("Not an integer. Please enter an integer.")
        continue

    if count < 0:
        print("Please enter a positive number.")
        continue

    elif count == 0:
        print("Please enter an integer greater than zero.")
        continue
    else:
        break


# times_run = 1
# random_words = []
# while times_run <= count:
#    word = secrets.choice(words)
#    random_words.append(word)
#    times_run += 1

def generate_words():
    random_words = []
    for i in range(count):
        word = secrets.choice(words)
        random_words.append(word)
    return random_words


# Function to apply upper and lower case to letters in a random sequence
def random_case(s):
    result = ''
    for char in s:
        case = random.randint(0, 1)
        if case == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


number = random.randint(0, 9)
punctuation = string.punctuation
str_to_list = list(punctuation)
special_character = secrets.choice(str_to_list)

# Join all items in the list to a string, separated by a separator
x = '-'.join(generate_words())

password = special_character + x + str(number)
xkcd_password = random_case(password)

print(f"Password generated: {xkcd_password}")
print(f"Password length: {len(xkcd_password)}\n")
pyperclip.copy(xkcd_password)
print("Password copied to clipboard.")
