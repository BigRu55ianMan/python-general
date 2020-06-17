import random

options = ['rock', 'paper', 'scissors']
cpuChoice = options[random.randint(0,2)]
cpuNumber = options.index(cpuChoice)

print()
userChoice = input('Choose your option (rock, paper or scissors): ')
print()

try:
    userNumber = options.index(userChoice)
except:
    print('Sorry', userChoice, 'is not a valid response, please try again.')
    print()
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

print()
print('gg')
print()
