# 程序结构

- `maze_error.py`中定义了所需的异常类
- `maze_factory.py`中为迷宫网格渲染的主程序
- `test.test_output.py`为对程序输出结果准确性的单元测试程序
- `test.test_validity.py`为对输入command有效性检查的单元测试程序
- `main.py`中为运行样例以及单元测试

# 如何运行

## 主程序

```python
from maze.maze_factory import MazeFactory

command = """3 3
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"""
maze = MazeFactory(command)
maze_test = maze.render()
print(maze_test)
```
输出：
```
[W] [W] [W] [W] [W] [W] [W]
[W] [R] [W] [R] [R] [R] [W]
[W] [R] [W] [R] [W] [R] [W]
[W] [R] [R] [R] [R] [R] [W]
[W] [W] [W] [R] [W] [R] [W]
[W] [R] [R] [R] [W] [R] [W]
[W] [W] [W] [W] [W] [W] [W]
```

**注：** 本程序在Linux下完成，输出使用的换行符为"\n"，在windows系统下可能会无法换行，特此备注

## 单元测试

```python
from maze.test.test_validity import TestValidity
from maze.test.test_output import TestOutput
import unittest

unittest.main()
```

# 容错性

为了保证程序的正常运行，我增加了输入的一些容错性，当出现以下情况时程序不会报错，并会自行处理和输出正确结果：

- 中间多个空格分隔
- 逗号后有多余的空格
- 首位冗余空格、换行符等x 
- 第二行末尾多出";"

# 申明

本人所提交的所有程序相关文件，均为本人独立完成，特此申明。

如有疑问，请联系：杨睿，邮箱：yangruipis@163.com，电话：18818231378