import pyinputplus

pieList = ['Pecan', 'Apple Crisp', 'Bean', 'Banofee', 'Black Bun', 'Blueberry', 'Buko', 'Burek', 'Tamale', 'Chocolate']
pieNum = [0] * len(pieList)
welcome = '\nWelcome to the House of Pies! Here are our pies and their respective indexes:'
theList = ', '.join('({}) {}'.format(index + 1, element) for index, element in enumerate(pieList)) + '.'

print(welcome)
print('-' * (len(welcome)-1),'\n')
print(theList)

while True:
    while True:
        userChoice = int(pyinputplus.inputInt('\nPlease select your pie using the pie\'s index: '))
        if userChoice < 1 or userChoice > len(pieList):
            print(userChoice, 'is not a valid index. Please try again.\n')
        else:
            break

    pieNum[userChoice - 1] += 1
    print('Great! We\'ll have that ' + pieList[userChoice - 1] + ' pie right out for you.')
    response = pyinputplus.inputYesNo('\nWould you like to make another order? ')
    if response == 'no':
        break

print('Here is your final order: \n')
print('\n'.join('{} {}'.format(index, element) for index, element in zip(pieNum, pieList)) + '\n')
