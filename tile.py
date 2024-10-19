class Tile:

    def __init__(self, suit, rank, tile_id):
        self.suit = suit
        self.rank = rank
        self.tile_id = tile_id
    
    def __repr__(self):
        title = f"{self.suit[0:2]}{self.rank}" if self.rank is not None else f"{self.suit[0:2]}"
        return title
        
