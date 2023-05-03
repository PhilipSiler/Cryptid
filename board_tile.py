import random

###GAME VARIABLES GO HERE
num_tiles = 108
num_structures = 8 #randomly selects a number between 5 and 8, for the # of structures on the board
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
        for index in self.structure_indices:
            self.pieces[index].structure = structures[0]
            structures.pop(0)

        #returns a randomly-ordered array of range(1,7) 
    def random_board_maker(self) -> list[list]:
        pieces = [[Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="WATER"),Tile(terrain="DESERT"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="DESERT"),Tile(terrain="DESERT",animal="BEAR"),Tile(terrain="DESERT",animal="BEAR"),Tile(terrain="FOREST",animal="BEAR")],
              [Tile(terrain="SWAMP",animal="COUGAR"),Tile(terrain="FOREST",animal="COUGAR"),Tile(terrain="FOREST",animal="COUGAR"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="SWAMP"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="DESERT")],
              [Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="WATER"),Tile(terrain="SWAMP",animal="COUGAR"),Tile(terrain="SWAMP",animal="COUGAR"),Tile(terrain="FOREST"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="MOUNTAIN",animal="COUGAR"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER")],
              [Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER",animal="COUGAR"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="FOREST",animal="COUGAR")],
              [Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN"),Tile(terrain="SWAMP"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="WATER"),Tile(terrain="MOUNTAIN"),Tile(terrain="MOUNTAIN",animal="BEAR"),Tile(terrain="DESERT"),Tile(terrain="DESERT"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER",animal="BEAR"),Tile(terrain="WATER",animal="BEAR")],
              [Tile(terrain="DESERT",animal="BEAR"),Tile(terrain="DESERT"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="MOUNTAIN",animal="BEAR"),Tile(terrain="MOUNTAIN"),Tile(terrain="SWAMP"),Tile(terrain="SWAMP"),Tile(terrain="FOREST"),Tile(terrain="FOREST"),Tile(terrain="MOUNTAIN"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="WATER"),Tile(terrain="FOREST")]
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
    random.shuffle(structures)
    return structures

structures = structure_maker()
board_arr = [None] * 108

#my_board = Board()