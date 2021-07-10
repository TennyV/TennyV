#Siriwat Vongtip


rooms = {
    'Mineshaft Entrance': {'North': 'Shaft One'},
    'Shaft One': {'West': 'Big Bob\'s Room', 'North': 'Shaft Two'},
    'Secret Room': {'North': 'Big Bob\'s Room'},
    'Big Bob\'s Room': {'South': 'Secret Room', 'East': 'Shaft One'},
    'Shaft Two': {'West': 'Dusty Johns Room', 'East': 'Steel Steve\'s Room'},
    'Steel Steve\'s Room': {'South': 'The Dog Room', 'West': 'Shaft Two'},
    'The Dog Room': {'South': 'Shaft Five', 'North': 'Steel Steve\'s Room'},
    'Shaft Five': {'North': 'The Dog Room'}
}
items = {
    'Mineshaft Entrance': 'No items here',
    'The Dog Room': 'nothing',
    'Shaft One': 'Gun',
    'Big Bob\'s Room': 'Whip',
    'Secret Room': 'Heart Container',
    'Shaft Two': 'Dynamite',
    'Steel Steve\'s Room': 'Bone',
    'Shaft Five': 'Disguise'

}
location = 'Mineshaft Entrance'
inventory = []
print('Welcome to the Sleepy Mines! \nCollect 6 items to win the game or be lost forever')
print('To move enter North, East, South, West, or the enter the name of the item identified in the room.')
print('Good Luck!')


def get_new_location(location, direction):
    new_location = location
    for i in rooms:
        if i == location:
            if direction in rooms[i]:
                new_location = rooms[i][direction]

    return new_location


while 1:
    print('You are in', location)
    if location == 'Dusty Johns Room':
        print('You lock gazes for what seems like an eternity!')
        print()
        if len(inventory) == 6:
            print('Congratulations!!!')
            print('ᕕ( ͡° ͜ʖ ͡°)ᕗ You win!')
        else:
            print('Sorry you died!!!  ɿ(｡･ɜ･)ɾⓌⓗⓨ? Try again?')
        break

    print('This room contains', items[location])
    print('Inventory List', inventory)
    print('(つ◉益◉)つ   (ง ͠° ͟ل͜ ͡°)ง')
    print('------------------------')
    direction = input('Enter item name to collect \nDirection you want to go \nEXIT to give up: ')
    if direction.lower() == items[location].lower():
        if items[location] not in inventory:
            inventory.append(items[location])
        continue
    direction = direction.capitalize()
    if direction == 'Exit':
        exit(0)
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  
        new_location = get_new_location(location, direction)
        if new_location == location:
            print('-----------------------------')
            print('Wrong way pick another route!')
        else:
            location = new_location
    else:
        print('Invalid direction!!')
