import random
import pyinputplus
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', ',',
 '.', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '@', '#',
 '$', '%', '^', '&', '*', '(', ')', '_', '+', '~', '`', '[', ']', '|', '{', '}',
 ';', "'", ':', '"', '<', '>', '/']

alphabetS = []

messageToken = ''
listToken = ''


def libraryCheck():
    for i in message:
        if i not in alphabet:
            alphabet.append(i)
        else:
            i = True

def libraryRandomizer():
    global listToken
    alphabetS = alphabet.copy()
    random.shuffle(alphabetS)
    for i in alphabetS:
        listToken += str(alphabet.index(i) + 10)
    print(alphabet)
    print()
    print(alphabetS)
    print()
    print(listToken)
    print(int(len(listToken)/2))
    print(len(alphabet))

libraryRandomizer()
