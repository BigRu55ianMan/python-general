import random
import time
import pyinputplus
import pyperclip
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', ',', '.',
 ' ', '1', '2', '3', '4', '5','6', '7', '8', '9', '0', '-', '=', '@', '#', '$',
 '%', '^', '&', '*', '(', ')','_', '+', '~', '`', '[', ']', '|', '{', '}', ';',
 "'", ':', '"', '<', '>', '/','\\','\t']
alphabetS = []
alphabetD = [0] * len(alphabet)

messageToken = ''
listToken = ''
messageD = ''

greeting = '\nWelcome to the greatest, safest encryptor known to me!\nI provide two services: encryption and decryption.'
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
    pyperclip.copy('{}.{}'.format(listToken, messageToken))

    print('\nChecking message.\n')
    time.sleep(1)
    print('Randomizing libraries.\n')
    time.sleep(1)
    print('Generating tokens.\n')
    time.sleep(1)
    print('Your code is: {}.{}\n'.format(listToken, messageToken))
    print('Your encrypted message code has been saved to your clipboard. Do not loose it!\nThank you for using my services.\n')



print(greeting)
userinput = pyinputplus.inputChoice(choices, '\nWould you like to encrypt or decrypt a message? ')

if userinput == 'e' or userinput == 'encrypt' or userinput == 'encryption':
    print('''You have selected: Encryption.

    Here are some rules that you must remember:
    1. Only lowercase letters can be decrypted, you can still have capital letters, but they will be saved as lowercase.
    2. Symbols outside of the standard US keyboard layout cannot be used.''')

    userMessage = input('\nPlease enter the text that you would like to Encript: ').lower()
    libraryRandomizer()
    messageEncryptor(userMessage)
else:
    print('You have selected: Decryption.')
    userKey = input('\nPlease enter your key: ').lower()
    decryptor(userKey)
