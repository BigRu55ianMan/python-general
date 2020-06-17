import random
import pyinputplus
import pyperclip

pyperclip.copy('python3 guess_the_number.py')

print()

rnum = random.randint(1, 20)
name = input('Enter your name: ')


print()

print(name + ', I have a number between 1 and 20 in my mind, would you like to guess it?')
response = pyinputplus.inputYesNo('Please reply with a yes or no: ')

print()

if response == 'no':
    print('Very well then. The number was', rnum, 'by the way.')
    print()
    print('Have a wonderfull day!')
    print()
    quit()
elif response == 'yes':
    print('Feeling lucky today huh. Very well then, you will have 5 guesses')

print()

for guessAttempts in range(0,5):
    guess = pyinputplus.inputNum('Please, take a guess: ')
    if guess < 1:
        print(guess, 'is lower than 1')
        print()
    elif guess > 20:
        print(guess, 'is greater than 20')
        print()
    elif guess > rnum:
        print('Unfortunately, your guess was too high')
        print()
    elif guess < rnum:
        print('Unfortunately, your guess was too low')
        print()
    else:
        print()
        break

if guess == rnum and guessAttempts == 0:
    print('Congratulations', name + '! You guessed the number I had in mind in 1 guess! Very impressive.')
    print()
elif guess == rnum:
    print('Congratulations', name + '! You guessed the number I had in mind in', guessAttempts, 'guesses! Impressive.')
    print()
else:
    print('Dear', name + ', it is with great concern and regret that I have to inform you that you failed to guees the number I had in mind.')
    print()
    print('The number I had in mind was:', rnum,)
    print('While your guess was:', guess)
    print()
