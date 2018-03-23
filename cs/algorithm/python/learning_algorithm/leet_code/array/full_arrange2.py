# -*- coding:utf-8 -*-

"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母
"""


class Solution:
    res = []

    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]

        self.full_range(ss, 0, len(ss) - 1)
        return self.res

    def full_range(self, ss, i, j):
        if i == j:
            self.res.append(ss)
        else:
            used = []
            for s in range(i, j + 1):
                if ss[s] in used:
                    continue
                else:
                    used.append(ss[s])
                ss = self.swap(ss, i, s)
                self.full_range(ss, i + 1, j)
                ss = self.swap(ss, i, s)

    def swap(self, ss, i, j):
        if i == j:
            return ss
        else:
            return ss[:i] + ss[j] + ss[i + 1:j] + ss[i] + ss[j + 1:]

if __name__ == '__main__':
    s = Solution()
    a = 'ab'
    s.Permutation(a)
    print(s.res)
