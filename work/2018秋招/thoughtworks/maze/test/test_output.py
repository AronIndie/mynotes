# -*- coding:utf-8 -*-

import unittest
from maze.maze_factory import MazeFactory
from maze.maze_error import *


class TestOutput(unittest.TestCase):

    def test_given_case(self):
        input_command = """3 3
        0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"""
        maze = MazeFactory(input_command)
        res_true = """
[W] [W] [W] [W] [W] [W] [W]
[W] [R] [W] [R] [R] [R] [W]
[W] [R] [W] [R] [W] [R] [W]
[W] [R] [R] [R] [R] [R] [W]
[W] [W] [W] [R] [W] [R] [W]
[W] [R] [R] [R] [W] [R] [W]
[W] [W] [W] [W] [W] [W] [W]
        """
        res = maze.render()
        self.assertEqual(res_true.strip(), res.strip())

    def test_other_case(self):
        command = """2 2
        0,0 0,1;0,0 1,0;1,1 0,1;1,1 1,0
        """
        maze = MazeFactory(command)
        res_true = """
[W] [W] [W] [W] [W]
[W] [R] [R] [R] [W]
[W] [R] [W] [R] [W]
[W] [R] [R] [R] [W]
[W] [W] [W] [W] [W]"""
        res = maze.render()
        self.assertEqual(res_true.strip(), res.strip())


if __name__ == '__main__':
    unittest.main()
