# -*- coding:utf-8 -*-

from maze.maze_error import *
import re


__all__ = [
    'MazeFactory',
]


class MazeFactory:

    def __init__(self, command: str):
        """
        迷宫渲染类
        :param command:要求
            - 第一行为迷宫尺寸，空格分割
            - 第二行为网格联通关系，关系内部为0,1 0,2的形式，关系之间用分号分割
        """
        self.shape = None
        self.connections = []
        self._parse_command(command)

    def _parse_command(self, command: str):
        """
        解析command，获取迷宫的行数和列数，以及cell之间的连接关系
        :param command: 输入的命令
        """
        self._clear()
        command_split = command.strip().replace("\r", "").split("\n")
        if len(command_split) != 2:
            raise IncorrectCommandFormatError("input line number = {}".format(len(command_split)))
        self.shape = self._check_shape(command_split[0].strip())

        connections_str = (i.strip() for i in command_split[1].rstrip(";").split(";"))
        for connection in connections_str:
            self.connections.append(self._check_connection(self.shape, connection))

    @staticmethod
    def split(s: str):
        """
        将文本按照空格切分，且剔除中间有多个空格的情况，输出切分之后的列表， "1    2" ---> ["1", "2"]
        :param s:  带切分的文本
        :return:   切分之后的文本列表
        """
        s = s.strip()
        return list(filter(lambda x: x != "", s.split(" ")))

    @staticmethod
    def replace_comma_space(s: str):
        """
        将逗号和其后面的空格替换为逗号， "1,  2" ---> "1,2"
        :param s:  文本
        :return:   替换后文本
        """
        reg = re.compile(',[ ]+')
        return reg.sub(",", s)

    @staticmethod
    def _check_shape(shape_line: str) -> tuple:
        """
        检查第一行是否有效，并且将行和列存入 self.shape 中
        :param shape_line: command的第一行
        :return: (int, int)
        """
        if " " in shape_line:
            line_split = MazeFactory.split(shape_line)
            if len(line_split) != 2:
                raise IncorrectCommandFormatError("shape number = {} in '{}'".format(len(line_split), shape_line))
            x, y = line_split
            if str.isdigit(x) and str.isdigit(y):
                return int(x), int(y)
            else:
                raise InvalidNumberFormatError("not int, row:{}, column:{}".format(x, y))
        else:
            raise IncorrectCommandFormatError("no space to split in '{}'".format(shape_line))

    @staticmethod
    def _check_connection(shape: tuple, connection: str) -> list:
        """
        检查第二行的连接是否有效，并且将连接关系 [(int, int), (int, int)] 输出
        :param shape:      command第一行中得到的形状
        :param connection: command第二行文本按照"；"分割的元素
        :return:  一对cell的连接关系，list
        """
        if " " not in connection:
            raise IncorrectCommandFormatError("no space to split in '{}'".format(connection))

        connection = MazeFactory.replace_comma_space(connection)
        conn_split = MazeFactory.split(connection)
        if len(conn_split) != 2:
            raise IncorrectCommandFormatError("cell number = {} in connection '{}'".format(len(conn_split), connection))

        cells = []
        for cell in conn_split:
            if "," not in cell:
                raise IncorrectCommandFormatError("no comma to split in '{}'".format(cell))
            cell_split = cell.split(",")
            if len(cell_split) != 2:
                raise IncorrectCommandFormatError("cell index number = {} in '{}'".format(len(cell_split), cell))
            num1, num2 = cell_split
            if (num1.startswith('-') and num1[1:] or num1).isdigit() and \
                    (num2.startswith('-') and num2[1:] or num2).isdigit():
                a = int(num1)
                b = int(num2)
                if (0 <= a < shape[0]) and (0 <= b < shape[1]):
                    cells.append((a, b))
                else:
                    raise OutOfRangeError("cell id in '{}' out of range".format(cell))
            else:
                raise InvalidNumberFormatError("not int, row:{}, column:{}".format(num1, num2))

        s = abs(cells[0][0] - cells[1][0]) + abs(cells[0][1] - cells[1][1])
        if s != 1:
            raise MazeFormatError("cells in '{}' is not connected".format(cells))
        return cells

    def _clear(self):
        self.shape = None
        self.connections = []

    @staticmethod
    def maze_init(shape: tuple) -> list:
        """
        根据迷宫的形状初始化一张迷宫，并且渲染出未联通时候的情况
        :param shape:  迷宫形状
        :return:  迷宫字符串列表
        """
        maze = [['[W]' for i in range(2 * shape[1] + 1)] for j in range(2 * shape[0] + 1)]
        for i in range(1, 2*shape[0]+1, 2):
            for j in range(1, 2*shape[1]+1, 2):
                maze[i][j] = '[R]'
        return maze

    def render(self):
        """
        渲染迷宫
        :return: 迷宫渲染最终字符串
        """
        maze = self.maze_init(self.shape)
        for conn in self.connections:
            cell1 = (2*conn[0][0]+1, 2*conn[0][1]+1)
            cell2 = (2*conn[1][0]+1, 2*conn[1][1]+1)
            maze[(cell1[0] + cell2[0]) // 2][(cell1[1] + cell2[1]) // 2] = '[R]'
        return self.display(maze)

    @staticmethod
    def display(maze: list) -> str:
        """
        将迷宫字符二维串列表显示为一整个字符串
        :param maze: 迷宫字符串二维列表
        :return: 最终结果
        """
        temp = [" ".join(i) for i in maze]
        return "\n".join(temp)
