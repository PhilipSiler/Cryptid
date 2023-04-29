import random

###GAME VARIABLES GO HERE
num_tiles = 108
num_structures = 8

class Board:
    def __init__(self) -> None:
        self.pieces = random.shuffle(self.pieces)
        self.structure_indices = random.sample(range(0,num_tiles), num_structures)

        #returns a randomly-ordered array of range(1,7) 
    def random_board_maker(self) -> list[int]:
        board_nums = [i for i in range(1,7)]
        random.shuffle(board_nums)
        return board_nums

    class Tile:
        def __init__(self, terrain, structure=None, animal=None, cubes=None) -> None:
            self.terrain_type = terrain
            self.structure = structure
            self.animal = animal
            self.cubes = cubes

    #big 18-hex pieces, indexed to zero (the big piece labeled 1 is index 0 here)
    pieces = [[Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="WATER"),Tile(terrain="DESERT"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="DESERT"),Tile(terrain="DESERT",animal="BEAR"),Tile(terrain="DESERT",animal="BEAR"),Tile(terrain="FOREST",animal="BEAR")],
              [Tile(terrain="SWAMP",animal="COUGAR"),Tile(terrain="FOREST",animal="COUGAR"),Tile(terrain="FOREST",animal="COUGAR"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="SWAMP"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="DESERT")],
              [Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="WATER"),Tile(terrain="SWAMP",animal="COUGAR"),Tile(terrain="SWAMP",animal="COUGAR"),Tile(terrain="FOREST"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="MOUNTAIN",animal="COUGAR"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER")],
              [Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER",animal="COUGAR"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="FOREST",animal="COUGAR")],
              [Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="SWAMP"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="WATER"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN",animal="BEAR"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER",animal="BEAR"),Tile(terrain="WATER",animal="BEAR")],
              [Tile(terrain="DESERT",animal="BEAR"),Tile(terrain="DESERT"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="MOUNTAIN",animal="BEAR"),Tile(terrain="MOUNTAIN"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="FOREST")]
             ]
    
    random.shuffle(pieces)

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
print(vars(my_board))