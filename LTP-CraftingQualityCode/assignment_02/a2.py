# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    
    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType 
        
        Initialize Rat with symbol at location (row, col). 

        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
    
    def set_location(self, row, col):
        """ 
        (Rat, int, int) -> NoneType 

        Set the location for Rat. 

        >>> rat = Rat('P', 1, 4)
        >>> rat.set_location(2, 3)
        >>> rat.row
        2
        >>> rat.col
        3
        """

        self.row = row
        self.col = col

    def eat_sprout(self):
        """
        (Rat) -> NoneType

        Eat a sprout, so the number of sprouts eaten increases by one for 
        the particular rat. 

        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.


if __name__ == '__main__':
    import doctest
    doctest.testmod()
