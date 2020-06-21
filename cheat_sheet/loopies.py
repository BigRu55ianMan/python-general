#while loops will run as long as the given parameter is True, or break is used.
while True:
    print('Hello World')
    break
print('\n')

#for loops iterate the given variable (i) through the values of a list (numbers), or a list-like value (range(0,3)).
numbers = [0, 1, 2]

for i in numbers:
    print(i)
print('\n')

for i in range(0,3):
    print(i)
print('\n')

#this for loop will print in a line, with the end= parameter being the string to be placed in between the variables.
for i in numbers:
    print(i, end=' ')
print('\n\n')

#for loops can iterate more than one variable through the values of thier respective lists usnig the zip() function.
words = ['banana', 'apple', 'watermelon']
numbers = [0, 1, 2]

for n, w in zip(numbers, words):
    print('I have {} {}s'.format(n,w))
print('\n')
