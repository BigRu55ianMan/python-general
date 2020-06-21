#while loops will run as long as the given parameter is True, or break is used.
while True:
    print('Hello World')
    break
print()

#for loops iterate the given variable (i) through the values of a list (numbers), or a list-like value (range(0,3))
numbers = [0, 1, 2]

for i in numbers:
    print(i)
print()

for i in range(0,3):
    print(i)
print()

#this for loop will print in a line, with the end= parameter being the string to be placed in between the variables
for i in numbers:
    print(i, end=' ')
print()
