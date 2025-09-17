"""""

Author: Sam Lewis
"""

import random

rooms = []
descriptions = []
exits = []  

input_file = "the-stilts.txt"
ghost_alive = True


f = open(input_file)
for line in f:
    line = line.strip()
    # if line is a comment skip it
    if not line:
        continue

    if line[0] == '#':
        continue
    
    tokens = line.split(":")
    if len(tokens) == 3:
        # this is a description line
        room_id = int(tokens[0].strip())
        name = tokens[1].strip()
        description = tokens[2].strip()

        while len(rooms) <= room_id:
            rooms.append(None)
            descriptions.append(None)

        rooms[room_id] = name
        descriptions[room_id] = description

    if len(tokens) == 5:
        room_id = int(tokens[0].strip())
        west = int(tokens[1].strip())
        north = int(tokens[2].strip())
        east = int(tokens[3].strip())
        south = int(tokens[4].strip())

        while len(exits) <= room_id:
            exits.append(None)

        exits[room_id] = [west, north, east, south]

f.close()

player_room = 0
ghost_room = random.randint(0, len(rooms) - 1)
portkey_room = random.randint(0, len(rooms) - 1)


def ghost_health():
    return 30

def player_health():
    return 30

def player_attack(ghost_hp):
    attack = input("choose your attack (1-3): ")
    if attack == "1":  
        damage = random.randint(5, 10)
        print("You punch the ghost and deal {} damage!".format(damage))
        ghost_hp -= damage
    elif attack == "2":  
        damage = random.randint(1, 15)
        print("You kick the ghost and deal {} damage!".format(damage))
        ghost_hp -= damage
    elif attack == "3":  
        damage = 7
        print("You use magic and deal {} damage!".format(damage))
        ghost_hp -= damage
    else:
        print("Try again.")
    return ghost_hp

def ghost_attack(player_hp):
    damage = random.randint(3, 13)
    print("The ghost attacks you and deals {} damage!".format(damage))
    player_hp -= damage
    return player_hp


while True:
    print("\nYou are in the {}.".format(rooms[player_room]))
    print(descriptions[player_room])
    move = input("Which direction do you want to go? (a/w/d/s): ").lower()
    directions = {'a': 0, 'w': 1, 'd': 2, 's': 3}
    if move in directions:
        next_room = exits[player_room][directions[move]]
        if next_room == -1:
            print("You can't go that way")
        else:
            player_room = next_room
    else:
        print("Try again. Enter w, a, s or d.")

    ghost_exits = exits[ghost_room]
    ghost_moves = [room for room in ghost_exits if room != -1]
    if ghost_moves:
        ghost_room = random.choice(ghost_moves)

    if player_room == portkey_room:
        print("You found the key, but here comes the ghost!")
        ghost_hp = ghost_health()
        player_hp = player_health()
        while ghost_hp > 0 and player_hp > 0:
            print("Player health: {}".format(player_hp))
            print("Ghost health: {}".format(ghost_hp))
            ghost_hp = player_attack(ghost_hp)
            if ghost_hp <= 0:
                print("You beat the ghost!")
                ghost_alive = False
                print("You win!")
                exit()
            player_hp = ghost_attack(player_hp)
            if player_hp <= 0:
                print("The ghost wins! Game over!")
                exit()

    if player_room == ghost_room:
        print("You found the ghost!")
        ghost_hp = ghost_health()
        player_hp = player_health()
        while ghost_hp > 0 and player_hp > 0:
            print("Player health: {}".format(player_hp))
            print("Ghost health: {}".format(ghost_hp))
            ghost_hp = player_attack(ghost_hp)
            if ghost_hp <= 0:
                print("You beat the ghost!")
                ghost_alive = False
                break
            player_hp = ghost_attack(player_hp)
            if player_hp <= 0:
                print("The ghost wins! Game over!")
                exit()

print(exits[player_room])
print(descriptions[player_room])
print(ghost_room)

