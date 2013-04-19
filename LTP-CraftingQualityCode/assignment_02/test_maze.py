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

    def test_move_rat_1_without_problem(self):
        """ Test if the rat moves in the given direction without any problem. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))

        m.move(m.rat_1, a2.NO_CHANGE, a2.RIGHT)
        expected_rat_1_row = 1
        expected_rat_1_col = 2
        expected_rat_1_num_sprouts_eaten = 0
        expected_maze_num_sprouts_left = 3

        self.assertEqual(expected_rat_1_row, m.rat_1.row)
        self.assertEqual(expected_rat_1_col, m.rat_1.col)
        self.assertEqual(expected_rat_1_num_sprouts_eaten, m.rat_1.num_sprouts_eaten)
        self.assertEqual(expected_maze_num_sprouts_left, m.num_sprouts_left)
    
    def test_move_rat_1_hits_wall(self):
        """ Test if the rat moves in the given direction and hits the wall. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))

        m.move(m.rat_1, a2.NO_CHANGE, a2.LEFT)
        expected_rat_1_row = 1
        expected_rat_1_col = 1
        expected_rat_1_num_sprouts_eaten = 0
        expected_maze_num_sprouts_left = 3

        self.assertEqual(expected_rat_1_row, m.rat_1.row)
        self.assertEqual(expected_rat_1_col, m.rat_1.col)
        self.assertEqual(expected_rat_1_num_sprouts_eaten, m.rat_1.num_sprouts_eaten)
        self.assertEqual(expected_maze_num_sprouts_left, m.num_sprouts_left)
    
    def test_move_rat_1_finds_sprout(self):
        """ Test if the rat moves in the given direction and finds a sprout. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        
        actual_character_at_location = m.maze[4][1]
        expected_character_at_location = a2.SPROUT
        self.assertEqual(expected_character_at_location, actual_character_at_location)

        m.move(m.rat_1, a2.DOWN, a2.NO_CHANGE)
        m.move(m.rat_1, a2.DOWN, a2.NO_CHANGE)
        m.move(m.rat_1, a2.DOWN, a2.NO_CHANGE)

        expected_rat_1_row = 4
        expected_rat_1_col = 1
        expected_rat_1_num_sprouts_eaten = 1
        expected_maze_num_sprouts_left = 2
        
        actual_character_at_new_location = m.maze[4][1]
        expected_character_at_new_location = a2.HALL
        self.assertEqual(expected_character_at_new_location, actual_character_at_new_location)

        self.assertEqual(expected_rat_1_row, m.rat_1.row)
        self.assertEqual(expected_rat_1_col, m.rat_1.col)
        self.assertEqual(expected_rat_1_num_sprouts_eaten, m.rat_1.num_sprouts_eaten)
        self.assertEqual(expected_maze_num_sprouts_left, m.num_sprouts_left)

    def test_str_repr(self):
        """ Test the string representation of the maze. """

        m = a2.Maze([['#', '#', '#', '#', '#', '#', '#'], 
                     ['#', '.', '.', '.', '.', '.', '#'], 
                     ['#', '.', '#', '#', '#', '.', '#'], 
                     ['#', '.', '.', '@', '#', '.', '#'], 
                     ['#', '@', '#', '.', '@', '.', '#'], 
                     ['#', '#', '#', '#', '#', '#', '#']], 
                     a2.Rat('J', 1, 1),
                     a2.Rat('P', 1, 4))
        actual = m.__str__()
        expected = '#######\n#J..P.#\n#.###.#\n#..@#.#\n#@#.@.#\n#######\nJ at (1, 1) ate 0 sprouts.\nP at (1, 4) ate 0 sprouts.' 

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)

