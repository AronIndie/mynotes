# -*- coding:utf-8 -*-

import unittest
from maze.maze_factory import MazeFactory
from maze.maze_error import *


class TestValidity(unittest.TestCase):

    def test_incorrect_command(self):
        s1 = "3 3 0,1 0,2; 1,1 1,2"
        s2 = """3 3
        0,1 0,2; 1,1 1,2;
        1,1 0,1"""
        s3 = """3 3 2
        0,1 0,2; 1,1 1,2;
        """
        s4 = """3 3
        0,1 0,2-1,1 1,2
        """
        s4 = """3 3
        0,1 0,2;;1,1 1,2
        """
        s5 = """3 3
        0,1 0,2;1,11,2"""
        self.assertRaises(IncorrectCommandFormatError, MazeFactory, s1)
        self.assertRaises(IncorrectCommandFormatError, MazeFactory, s2)
        self.assertRaises(IncorrectCommandFormatError, MazeFactory, s3)
        self.assertRaises(IncorrectCommandFormatError, MazeFactory, s4)
        self.assertRaises(IncorrectCommandFormatError, MazeFactory, s5)

    def test_number_format(self):
        s1 = """3 a
        0,1 0,2; 1,1 1,2
        """
        s2 = """3 a
        0,1 0,2; 1,1 b-2,2
        """
        self.assertRaises(InvalidNumberFormatError, MazeFactory, s1)
        self.assertRaises(InvalidNumberFormatError, MazeFactory, s2)

    def test_out_of_range(self):
        s1 = """3 3
        0, 1 -1, 1
        """
        s2 = """3 3
        0, 2 0,3 
        """
        self.assertRaises(OutOfRangeError, MazeFactory, s1)
        self.assertRaises(OutOfRangeError, MazeFactory, s2)

    def test_maze_format(self):
        s1 = """3 3
        0,0 1,1
        """
        s2 = """3 3
        0,0 0,2
        """
        self.assertRaises(MazeFormatError, MazeFactory, s1)
        self.assertRaises(MazeFormatError, MazeFactory, s2)


if __name__ == '__main__':
    unittest.main()
