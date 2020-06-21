import re

prompt = input('\nEnter a phone number to check: ')
print()

def isPhoneNumber2(text):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.findall(text)
    if mo:
        for i in mo:
            print('Phone number found:', i, '\n')
    else:
        print('No phone numbers were found.\n')


isPhoneNumber2(prompt)
