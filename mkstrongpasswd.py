import random
import string
from random_words import RandomWords

rw = RandomWords()
word1 = rw.random_words()
word2 = rw.random_words()
word3 = rw.random_words()
word4 = rw.random_words()
word5 = rw.random_words()
sep = ['-']
num = random.randint(0, 9)
#punc = string.punctuation

list1 = word1 + sep + word2 + sep + word3 + sep + word4 + sep + word5
passwd = ''.join(list1)
mkpasswd = passwd + str(num)
print("Password generated: " + mkpasswd)
#print(punc)