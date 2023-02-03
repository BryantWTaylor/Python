friends = []
friend = ''

while friend != 'end':
    friend = input('Type the name of a friend: ')
    if friend != 'end':
        friends.append(friend)

print('Your friends are:')
for friend in friends:
    print(friend)