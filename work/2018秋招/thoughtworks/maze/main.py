# -*- coding:utf-8 -*-

from maze.maze_factory import MazeFactory
from maze.test.test_validity import TestValidity
from maze.test.test_output import TestOutput
import unittest


def main():
    # A Simple Case
    command = """3 3
    0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"""
    maze = MazeFactory(command)
    print(maze.render())

    # Unit test for command validity and output correctness
    unittest.main()


if __name__ == '__main__':
    main()
