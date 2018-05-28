# -*- coding:utf-8 -*-

"""
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        i = len(s) - 1
        # 遍历一遍得到空格数目
        space_count = len(filter(lambda x: x==" ", s))
        s += [""] * space_count * 2
        j = len(s) - 1

        while i >= 0 and j >= 0:

            if s[i] != " ":
                s[j] = s[i]
                j -= 1
                i -= 1
            else:
                s[j] = "0"
                s[j-1] = "2"
                s[j-2] = "%"
                j -= 3
                i -= 1

        return "".join(s)
