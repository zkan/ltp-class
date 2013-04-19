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
        
        Initialize a rat with symbol at location (row, col). 

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

        Set the location for the rat. 

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
        the rat. 

        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str

        Return a string representation of the rat in this format 
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat.__str__()
        'P at (1, 4) ate 2 sprouts.'
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, 
                                                           self.row, 
                                                           self.col, 
                                                           self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

    def __init__(self, maze, rat_1, rat_2):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize a maze with a given maze and two rats. 

        >>> m = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1), Rat('P', 1, 4)) 
        >>> m.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> m.rat_1.symbol
        'J'
        >>> m.rat_1.row
        1
        >>> m.rat_1.col
        1
        >>> m.rat_2.symbol
        'P'
        >>> m.rat_2.row
        1
        >>> m.rat_2.col
        4
        >>> m.num_sprouts_left
        3
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0

        for l in self.maze:
            for item in l:
                if item == SPROUT: 
                    self.num_sprouts_left += 1

    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze. 

        >>> m = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1), Rat('P', 1, 4)) 
        >>> m.is_wall(0, 0)
        True
        >>> m.is_wall(1, 4)
        False
        """

        if self.maze[row][col] == WALL:
            return True
        else:
            return False

    def get_character(self, row, col):
        """
        (Maze, int, int) -> str

        Return the character in the maze at the given row and column. If there is a rat 
        at that location, then its character should be returned rather than HALL. 

        >>> m = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1), Rat('P', 1, 4)) 
        >>> m.get_character(1, 1)
        'J'
        >>> m.get_character(1, 4)
        'P'
        >>> m.get_character(1, 2)
        '.'
        """

        # Check the location of rat 1
        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol

        if self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol

        return HALL


if __name__ == '__main__':
    import doctest
    doctest.testmod()

