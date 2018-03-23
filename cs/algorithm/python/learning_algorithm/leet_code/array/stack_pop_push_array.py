# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        flag = True
        while pushV:
            if flag:
                stack.append(pushV.pop(0))
            if popV[0] == stack[-1]:
                stack.pop()
                popV.pop(0)
                if pushV and pushV[0] == popV[0]:
                    flag = True
                else:
                    flag= False

            else:
                if not pushV:
                    return False
                else:
                    flag = True
        stack.reverse()
        if stack == popV:
            return True
        return False

if __name__ == '__main__':
    a = [1,2,3,4,5]
    b = [4,3,5,1,2]
    s = Solution()
    print(s.IsPopOrder(a, b))