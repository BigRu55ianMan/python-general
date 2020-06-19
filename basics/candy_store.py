import pyinputplus

candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
candy_cart = []

print()

print('Here is the candy you can buy: \n')

for i in candy_list:
    print('[' + str(candy_list.index(i)) + ']', i)
print()

while True:
    allowance = int(input('What is your allowance? '))
    if allowance < 1:
        print('Sorry, you cannot spend less than $1. Please try again. \n')
    else:
        break
        print()


for k in range(0, allowance):
    while True:
        choice = int(input('Please select a candy to add to your cart: '))
        if choice > 8 or choice < 0:
            print('Sorry, the index you entered does not seem to exist in our database. Please try again. \n')
        else:
            break
    print(candy_list[choice], 'was added to your cart \n')
    candy_cart.append(candy_list[choice])

print('Here is your cart: \n')

for h in candy_cart:
    print(h)
print()
