import random

options = ['rock', 'paper', 'scissors']
cpuChoice = options[random.randint(0,2)]
cpuNumber = options.index(cpuChoice)

userChoice = input('\nChoose your option (rock, paper or scissors): ')

try:
    userNumber = options.index(userChoice)
except:
    print('\nSorry', userChoice, 'is not a valid response, please try again.')
    quit()

if userNumber == cpuNumber:
    print('How bizzarre! We both chose', cpuChoice + '.')
elif userNumber == 2 and cpuNumber == 0 :
    print('Unfortunately, my rock beats your scissors.')
elif userNumber == 0 and cpuNumber == 2:
    print('Congratulations! Your rock beats my scissors')
elif userNumber < cpuNumber:
    print('Unfrotunately, my', cpuChoice, 'beats your', userChoice + '.')
elif userNumber > cpuNumber:
    print('Congratulations! Your', userChoice, 'beats my', cpuChoice + '.' )

print('\ngg\n')
