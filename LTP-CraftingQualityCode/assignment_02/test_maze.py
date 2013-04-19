import a2
import unittest

class TestMazeMethods(unittest.TestCase): 
    """ Test class for methods in class Maze. """ 

    def test_init_maze(self): 
        """ Test __init__ with a given maze, rat_1, and rat_2. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        expected_maze = [['#', '#', '#', '#', '#', '#', '#'], 
                         ['#', '.', '.', '.', '.', '.', '#'], 
                         ['#', '.', '#', '#', '#', '.', '#'], 
                         ['#', '.', '.', '@', '#', '.', '#'], 
                         ['#', '@', '#', '.', '@', '.', '#'], 
                         ['#', '#', '#', '#', '#', '#', '#']]
        expected_rat_1 = a2.Rat('J', 1, 1)
        expected_rat_2 = a2.Rat('P', 1, 4)
        expected_num_sprouts_left = 3

        self.assertEqual(expected_maze, m.maze)
        self.assertTrue(expected_rat_1.__eq__(m.rat_1))
        self.assertTrue(expected_rat_2.__eq__(m.rat_2))
        self.assertEqual(expected_num_sprouts_left, m.num_sprouts_left)
   
    def test_is_really_wall(self):
        """ Test is_wall to check if there is a wall at the given row and column of the maze. 
        Suppose (0, 0) is given. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        
        self.assertTrue(m.is_wall(0, 0))

    def test_is_not_wall(self):
        """ Test is_wall to check if there is NOT a wall at the given row and column of the maze. 
        Suppose (1, 4) is given. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        
        self.assertFalse(m.is_wall(1, 4))

    def test_get_character(self):
        """ Test if there is a rat at the location, then its character should be returned rather than HALL. 
        Suppose (1, 4) is given. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        
        self.assertEqual(m.get_character(1, 4), 'P')
    
    def test_get_not_character(self):
        """ Test if there is NOT a rat at the location, then return HALL. 
        Suppose (1, 2) is given. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        
        self.assertEqual(m.get_character(1, 2), a2.HALL)


if __name__ == '__main__':
    unittest.main(exit=False)
