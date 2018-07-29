# -*- coding:utf-8 -*-


__all__ = [
    'InvalidNumberFormatError',
    'OutOfRangeError',
    'MazeFormatError',
    'IncorrectCommandFormatError',
]


class InvalidNumberFormatError(ValueError):

    __doc__ = "无效的数字:输入的字符串无法正确的转换为数字"

    def __init__(self, err=""):
        super(InvalidNumberFormatError, self).__init__("Invalid number format​. " + err)


class OutOfRangeError(IndexError):

    __doc__ = "数字超出预定范围:数字超出了允许的范围,例如为负数等"

    def __init__(self, err=""):
        super(OutOfRangeError, self).__init__("Number out of range. " + err)


class MazeError(Exception):

    __doc__ = "迷宫错误父类，任何和迷宫层面相关的错误均继承该异常类"

    def __init__(self, err=""):
        super(MazeError, self).__init__(err)


class IncorrectCommandFormatError(MazeError):

    __doc__ = "格式错误:输入命令的格式不符合约定"

    def __init__(self, err=""):
        super(IncorrectCommandFormatError, self).__init__("Incorrect command format. " + err)


class MazeFormatError(MazeError):

    __doc__ = "连通性错误:如果两个网格无法连通,则属于这种错误"

    def __init__(self, err=""):
        super(MazeFormatError, self).__init__("Maze format error. " + err)
