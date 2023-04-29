import random

###GAME VARIABLES GO HERE
num_tiles = 108
num_structures = 8
class Tile:
        def __init__(self, terrain, structure=None, animal=None, cubes=None) -> None:
            self.terrain_type = terrain
            self.structure = structure
            self.animal = animal
            self.cubes = cubes

class Board:
    def __init__(self) -> None:
        self.pieces = self.random_board_maker()#random.shuffle(self.pieces)
        self.structure_indices = random.sample(range(0,num_tiles), num_structures)

        #returns a randomly-ordered array of range(1,7) 
    def random_board_maker(self) -> list[list]:
        pieces = [[Tile("WATER"),Tile("WATER"),Tile("WATER"),Tile("WATER"),Tile("FOREST"),Tile("FOREST"),Tile("SWAMP"),Tile("SWAMP"),Tile("WATER"),Tile("DESERT"),Tile("FOREST"),Tile("FOREST"),Tile("SWAMP"),Tile("SWAMP"),Tile("DESERT"),Tile("DESERT"),Tile("DESERT"),Tile("FOREST")],
              [Tile("SWAMP"),Tile("FOREST"),Tile("FOREST"),Tile("FOREST"),Tile("FOREST"),Tile("FOREST"),Tile("SWAMP"),Tile("SWAMP"),Tile("FOREST"),Tile("DESERT"),Tile("DESERT"),Tile("DESERT"),Tile("SWAMP"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("DESERT")],
              [Tile("SWAMP"),Tile("SWAMP"),Tile("FOREST"),Tile("FOREST"),Tile("FOREST"),Tile("WATER"),Tile("SWAMP"),Tile("SWAMP"),Tile("FOREST"),Tile("MOUNTAIN"),Tile("WATER"),Tile("WATER"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("WATER"),Tile("WATER"),],
              [Tile("DESERT"),Tile("DESERT"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("DESERT"),Tile("DESERT"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("WATER"),Tile("WATER"),Tile("DESERT"),Tile("DESERT"),Tile("DESERT"),Tile("FOREST"),Tile("FOREST"),Tile("FOREST"),],
              [Tile("SWAMP"),Tile("SWAMP"),Tile("SWAMP"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("DESERT"),Tile("DESERT"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("WATER"),Tile("WATER"),Tile("DESERT"),Tile("DESERT"),Tile("DESERT"),Tile("FOREST"),Tile("FOREST"),Tile("FOREST"),],
              [Tile("DESERT"),Tile("DESERT"),Tile("SWAMP"),Tile("SWAMP"),Tile("SWAMP"),Tile("FOREST"),Tile("MOUNTAIN"),Tile("MOUNTAIN"),Tile("SWAMP"),Tile("SWAMP"),Tile("FOREST"),Tile("FOREST"),Tile("MOUNTAIN"),Tile("WATER"),Tile("WATER"),Tile("WATER"),Tile("WATER"),Tile("FOREST"),]
             ]
        random.shuffle(pieces)
        pieces_combined = []
        for piece in pieces:
            if random.choice([True, False]):
                piece = piece[::-1]
            pieces_combined.extend(piece)
        return pieces_combined

class Structure:
    def __init__(self, color, type) -> None:
        self.color = color
        self.type = type

def structure_maker() -> list[Structure]:
    structures = []
    colors = ["Blue", "Black", "White", "Green"]
    types = ["Abandoned Shack", "Standing Stone"]
    for color in colors:
        for type in types:
            structures.append(Structure(color, type))
    return structures

#returns all possible structures
def structure_maker() -> list[Structure]:
    structures = []
    colors = ["Blue", "Black", "White", "Green"]
    types = ["Abandoned Shack", "Standing Stone"]
    for color in colors:
        for type in types:
            structures.append(Structure(color, type))
    return structures

structures = structure_maker()
board_arr = [None] * 108

my_board = Board()
for hex in my_board.pieces:
    print(vars(hex))