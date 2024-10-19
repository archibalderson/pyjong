from tile import Tile
import random

def make_batch(suit, rank, wall):
    # creates 4 identical tiles with an assigned ID (0-3) and adds them to the wall 
    i = 0
    for tile in range(4):
        temp = Tile(suit, rank, tile)
        wall.append(temp)

def make_kong(wall):
    # removes 16 tiles from the wall (which should be twittered at this stage) and adds them to the kong box
    kong_box = []
    for tile in range(16):
        kong_box.append(wall.pop())
    return kong_box

def make_hand(wall):
    # creates a hand for players to use
    hand = []
    # add check for which wind to decide initial tile 14
    for tile in range(14):
        hand.append(wall.pop())
    return hand

def make_wall():
    # creates wall containing all necessary tiles and randomises ("twitters") them 
    suits = ["bamboo", "character", "plates"]
    winds = ["north", "east", "south", "west"]
    dragons = ["red", "green", "white"]

    wall = []

    for suit in suits:
        for rank in range(1, 10):
            make_batch(suit, rank, wall)

    for wind in winds:
        make_batch(wind, None, wall)

    for dragon in dragons:
        make_batch(dragon, None, wall)
    
    random.shuffle(wall)
    return wall

def draw_tile(wall):
    # removes tile from wall
    return wall.pop()

def discard_tile(tile):
    # sets currently visible table tile to tile most recently discarded  
    table_tile = tile 
    print(f"Tile on the table is now: {table_tile}")

def swap(new_tile, current_hand):
    # asks player for tile to be swapped with incoming tile
    print(f"\nCurrent hand: {current_hand}")

    while True:
        try:
            discard_index = int(input(f"Choose a tile from your hand to discard (0-{len(current_hand)-1}): "))
            
            if 0 <= discard_index < len(current_hand):
                discarded_tile = current_hand.pop(discard_index)
                discard_tile(discarded_tile)
                current_hand.append(new_tile)
                current_hand.sort(key=str)
                break
            else:
                print("Invalid tile, please enter again")
        except ValueError:
            print("Please enter a valid number")
    
    print(f"\nNew hand: {current_hand}")
    return current_hand

def start_turn(hand, wall):
    # draws new tile from the wall and awaits player interaction
    print(f"Current hand: {hand}")
    drawn_tile = draw_tile(wall)
    while True:
        answer = input(f"\nNew tile is {drawn_tile}, keep or discard? (K/D)")
        if answer.lower() == 'k':
            swap(drawn_tile, hand)
            break
        elif answer.lower() == 'd':
            discard_tile(drawn_tile)
            break
        else:
            print("Invalid input") 




wall = make_wall()
table_tile = None


kong_box = make_kong(wall)

player_hand = make_hand(wall)
player_hand.sort(key=str)

print(player_hand)
start_turn(player_hand, wall)

