import pprint

print()
message = input('Enter any message and I will count every character: ')
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    count[character] += 1

print()
pprint.pprint(count)
print()
