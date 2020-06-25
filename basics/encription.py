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
messageD = ''

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

def decryptor(listKey, messageKey):
    global alphabetD
    global messageD
    m, l = 0, 0
    k, g = 2, 2

    for i in range(int(len(listKey)/2)):
        alphabetD[int(listKey[l:g])-10] = alphabet[i]
        l += 2
        g += 2

    for i in range(int(len(messageKey)/2)):
        messageD += alphabetD[int(messageKey[m:k])-10]
        m += 2
        k += 2

    for i in range(int(len(messageKey)/2)):
        messageD

def messageEncryptor(text):
    global messageToken
    for i in text:
        messageToken += str(alphabetS.index(i) + 10)
