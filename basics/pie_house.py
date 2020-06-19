import pyinputplus

pieList = ['Pecan', 'Apple Crisp', 'Bean', 'Banofee', 'Black Bun', 'Blueberry', 'Buko', 'Burek', 'Tamale', 'Chocolate']
pieNum = [0] * len(pieList)
welcome = '\nWelcome to the House of Pies! Here are our pies and their respective indexes:'

print(welcome)
print('-' * (len(welcome)-1),'\n')

for index, element in enumerate(pieList):
    print('(' + str(index +1 ) + ')', str(element) + ', ', end='')

print()
print()

while True:
    while True:
        userChoice = int(pyinputplus.inputInt('\nPlease select your pie using the pie\'s index: '))
        if userChoice > len(pieList) or userChoice < 1:
            print('That index is not on the list, please try again.\n')
        else:
            break

    pieNum[userChoice - 1] += 1
    print('Great! We\'ll have that ' + pieList[userChoice - 1] + ' pie right out for you.\n')
    response = pyinputplus.inputYesNo('\nWould you like to make another order? ')
    if response == 'no':
        print()
        break
    else:
        print()

print('Here is your final order: \n')

for i in range(0, len(pieList)):
    print(pieNum[i], pieList[i])

print()
