import random

class Tile:

    def __init__(self, suit, rank, tile_id):
        self.suit = suit
        self.rank = rank
        self.tile_id = tile_id
    
    def __repr__(self):
        title = f"{self.rank}{self.suit[0:2]}" if self.rank is not None else f"{self.suit[0:2]}"
        return title
        
    def getTile(self):
        return f"{self.rank} of {self.suit} (ID: {self.tile_id})" if self.rank is not None else f"{self.suit} tild (ID: {self.tile_id})"




