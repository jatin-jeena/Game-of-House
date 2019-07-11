dict = {'Bedroom': [['Apple', 'Bat'], {1: [1, 'Balcony'], 2: [0, "No path available"], 3: [0, "No path available"], 4: [1, "Bathroom"]}],
        'Balcony': [['Mango', 'Clothes'], {1: [1, 'Drawing Room'], 2: [1, "Bedroom"], 3: [0, "No path available"], 4: [1, "Gallery"]}],
        'Drawing Room': [['Grapes', 'Phone'], {1: [0, 'No path available'], 2: [1, "Balcony"], 3: [0, "No path available"], 4: [1, "Kitchen"]}],
        'Bathroom': [['Bucket', 'Towel'], {1: [1, 'Gallery'], 2: [0, "No path available"], 3: [1, "Bedroom"], 4: [0, "No path available"]}],
        'Gallery': [['Painting', 'Watch'], {1: [1, 'Kitchen'], 2: [1, "Bathroom"], 3: [1, "Balcony"], 4: [1, "Lawn"]}],
        'Kitchen': [['Chocolate', 'Cold Drink'], {1: [0, 'No path available'], 2: [1, "Gallery"], 3: [1, "Drawing Room"], 4: [1, "Garage"]}],
        'Lawn': [['Chair', 'Table'], {1: [1, 'Garage'], 2: [0, "No path available"], 3: [1, "Gallery"], 4: [0, "No path available"]}],
        'Garage': [['Cycle', 'ToolBox'], {1: [0, 'No path available'], 2: [1, "Lawn"], 3: [1, "Kitchen"], 4: [0, "No path available"]}],
        'Road': [['Garbage', 'Leaves'], {1: [0, 'No path available'], 2: [0, "No path available"], 3: [1, "Lawn"], 4: [0, 'No path available']}],
        }


# Inventory stores the items present in the Inventory.Stores the items which is picked by
# the individual

Inventory = list()


# Displays the current state. Displays current location and directions available from present state
def Look(currenta):
    global dict
    around = list()
    part = dict[currenta]
    directions = part[1]
    d = directions.keys()
    for i in d:
        if directions[i][0] == 1:
            if i == 1:
                around.append(["East: " + str(directions[i][1])])
            if i == 2:
                around.append(["West: " + str(directions[i][1])])
            if i == 3:
                around.append(["North: " + str(directions[i][1])])
            if i == 4:
                around.append(["South: " + str(directions[i][1])])
    print("present Direcitons")
    print(*around)
    return around


# Moves the person from one location to another and also displays current location and available directions
def Move(currenta, move):
    global dict
    global current
    directions = Look(currenta)
    options = list()
    d = list()
    for i in directions:
        options.append(i[0].split(':')[1])
        d.append(i[0].split(':')[0])
    for i in range(directions.__len__()):
        if move == d[i]:
            go = options[i]
    print("Current Location : ", go)
    Look(go.strip())
    current = go
    return str(current)


# Picks the items form the current location and adds it to inventory .It also displays inventory and current location
def Pick(current, item):
    global Inventory
    global dict
    available = dict[current][0]
    for i in available:
        if i == item:
            available.remove(str(i))
            Inventory.append(item)
            dict[current][0] = available
            break
    print("Inventory :", Inventory)
    print("Current Position :", current)


# Drops an item in the location and also removes that item from the inventory.Adds dropped item to the item list of
#the location.
def Drop(current, item):
    global Inventory
    global dict
    Inventory.remove(item)
    available = dict[current][0]
    available.append(item)
    dict[current][0] = available
    print("Inventory :", Inventory)
    print("Current Position :", current)


current = 'Road'

currentdir = Look(current)
print("current postion ", current)
print("Current Directions available :- ")
print(*currentdir)
print("Inventory :", Inventory)
while (1):
    print("Press 1 for Drop")
    print("Press 2 for Pick")
    print("Press 3 for Move")
    a = int(input())
    if a == 1:
        tobe = input("Enter item to be dropped")
        Drop(current, tobe)
    elif a == 3:
        tobe = input("Enter the Direction to move")
        current = Move(current, tobe)
        current = current.strip()
    else:
        tobe = input("Enter item to pick")
        Pick(current, tobe)













