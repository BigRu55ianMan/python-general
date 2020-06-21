#while loops will run as long as the given parameter is True, or break is used.
while True:
    print('Hello World!')
    break
print('\n')

#try except will go the 'except' route if the 'try' route returns an error (syntax, traceback etc.). Works wierdly with other loops, so i don't know if it's too usable.
try:
    int('hello')
except:
    print('\'Hello\' is not an integer')
print('\n')

#if statements will go through each parameter until a True value is returned
k = 0

if k == 1:
    print('False')
elif k == 0:
    print('True')
print('\n')

#if the value is None, the if parameter is skipped.
if None:
    print('None')
else:
    print('None will go the \'else\' route')
print('\n')

#for loops iterate the given variable (i) through the values of a list (numbers), or a list-like value (range(0,3)).
numbers = [0, 1, 2]

for i in numbers:
    print(i)
print('\n')

for i in range(0,3):
    print(i)
print('\n')

#this for loop will print in a line, with the end= parameter being the string to be placed in between the variables. end= must be turned off after the loop.
for i in numbers:
    print(i, end=' ')
print('\n\n')

#for loops can iterate more than one variable through the values of thier respective lists usnig the zip() function.
words = ['banana', 'apple', 'watermelon']
numbers = [0, 1, 2]

for n, w in zip(numbers, words):
    print('I have {} {}s,'.format(n, w), end=' ')
print('\n\n')

#this wierd for loop that Igor made is the same as the previous one, but it allows the last character to be different from the rest of the loop.
print(', '.join('I have {} {}s'.format(n, w) for n, w in zip(numbers, words)) + '.')
print('\n')
