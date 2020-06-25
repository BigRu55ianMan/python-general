import random
import time
import pyinputplus
import pyperclip
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', ',', '.',
 ' ', '1', '2', '3', '4', '5','6', '7', '8', '9', '0', '-', '=', '@', '#', '$',
 '%', '^', '&', '*', '(', ')','_', '+', '~', '`', '[', ']', '|', '{', '}', ';',
 "'", ':', '"', '<', '>', '/','\\']
alphabetS = []
alphabetD = [0] * len(alphabet)

messageToken = ''
listToken = ''
messageD = ''

greeting = '\nWelcome to the greatest, safest ecnryptor known to me!\nI provide two services: encryption and decryption.'
choices = ['decryption', 'decrypt', 'd', 'encrypt', 'encryption', 'e']

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

def decryptor(key):
    global alphabetD
    global messageD

    listKey = key[:key.find('.')]
    messageKey = key[key.find('.')+1:]

    m, l = 0, 0
    k, g = 2, 2

    for i in range(int(len(listKey)/2)):
        alphabetD[int(key[l:g])-10] = alphabet[i]
        l += 2
        g += 2

    for i in range(int(len(messageKey)/2)):
        messageD += str(alphabetD[int(messageKey[m:k])-10])
        m += 2
        k += 2

def messageEncryptor(text):
    global messageToken
    for i in text:
        messageToken += str(alphabetS.index(i) + 10)
    print('Fantastic. Your encryption code is: {}.{}\n\nYour code was also saved into your clipboard.\nThank you for using my services.\n'.format(listToken, messageToken))
    pyperclip.copy('{}.{}'.format(listToken, messageToken))

print(greeting)
userinput = pyinputplus.inputChoice(choices, '\nWould you like to encrypt or decrypt a message? ')

if userinput == 'e' or userinput == 'encrypt' or userinput == 'encryption':
    print('You have selected: Encryption.')
    libraryRandomizer()
    messageEncryptor(input('\nPlease enter the text that you would like to Encript: '))
else:
    print('You have selected: Decryption.')
    userKey = input('\nPlease enter your key: ').lower()
    decryptor(userKey)
