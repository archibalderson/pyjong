from tile import Tile
import random

def make_batch(suit, rank):
    i = 0
    for tile in range(4):
        temp = Tile(suit, rank, tile)
        wall.append(temp)

def make_kong():
    kong_box = []
    for tile in range(16):
        kong_box.append(wall.pop())
    return kong_box

def make_hand():
    hand = []
    # add check for which wind to decide initial tile 14
    for tile in range(14):
        hand.append(wall.pop())
    return hand

def make_wall():
    suits = ["bamboo", "character", "plates"]
    winds = ["north", "east", "south", "west"]
    dragons = ["red", "green", "white"]

    wall = []

    for suit in suits:
        for rank in range(1, 10):
            make_batch(suit, rank)

    for wind in winds:
        make_batch(wind, None)

    for dragon in dragons:
        make_batch(dragon, None)
    
    random.shuffle(wall)
    return wall


wall = make_wall()

kong_box = make_kong()

player_hand = make_hand()
