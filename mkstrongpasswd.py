import random
import string
from random_words import RandomWords


def random_case(word):
    result = ''
    for char in word:
        case = random.randint(0, 1)
        if case == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


rw = RandomWords()
word1 = rw.random_words()
word2 = rw.random_words()
word3 = rw.random_words()
word4 = rw.random_words()
word5 = rw.random_words()

sep = ['-']
num = random.randint(0, 9)
punctuation = string.punctuation
str_to_list = list(punctuation)
special_char = random.choice(str_to_list)

list1 = word1 + sep + word2 + sep + word3 + sep + word4 + sep + word5
passwd = ''.join(list1)
mkpasswd = passwd + str(num) + special_char

print(f"Password generated: {random_case(mkpasswd)}")
print(f"Password length: {len(mkpasswd)}")