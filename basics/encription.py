import random
import time
import pyperclip
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', ',',
 '.', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '@', '#',
 '$', '%', '^', '&', '*', '(', ')', '_', '+', '~', '`', '[', ']', '|', '{', '}',
 ';', "'", ':', '"', '<', '>', '/']
alphabetS = []
alphabetD = [0] * len(alphabet)

messageToken = ''
listToken = ''

message = input('Please enter the message that you would like to encrypt: ')


def libraryCheck(text):
    for i in text:
        if i not in alphabet:
            alphabet.append(i)
        else:
            i = True

def libraryRandomizer():
    global listToken
    global alphabetS

    alphabetS = alphabet.copy()
    random.shuffle(alphabetS)
    for i in alphabet:
        listToken += str(alphabetS.index(i) + 10)

def messageEncryptor(text):
    global messageToken
    for i in text:
        messageToken += str(alphabetS.index(i) + 10)

def libraryDeRandomizer(key):
    global alphabetD
    l = 0
    g = 2

    for i in range(int(len(key )/2)):
        print(yuh[l:g])
        l += 2
        g += 2

yuh = '122334455667788990'

libraryDeRandomizer()
