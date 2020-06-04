import pyinputplus as pyip

print()
print('Is it a prime number or not?')
n = pyip.inputNum('enter an integer: ')
key = 1
print()

k = n - 1
z = n - 1
primelist = []
intlist = []
print()

while n % k != 0:
    primelist.append(k)
    k = k-1

while z > 1:
    intlist.append(z)
    z = z-1

primelist.sort()
intlist.sort()

if intlist == primelist:
    print(n, 'is a prime number')
else:
    print(n, 'is not a prime number')

print()
print('bye bye')
print()
#need to get rid of easy candidates like even and divisible by 3 5 7 etc
