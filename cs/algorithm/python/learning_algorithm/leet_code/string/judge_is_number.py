class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        s = s.replace(" ", "").lower()
        if "e" not in s:
            return self.isFloat(s)
        else:
            sp = s.split("e")
            if len(sp) != 2:
                return False
            else:
                return self.isFloat(sp[0]) and self.isInt(sp[1])

    number = ['1', '2', '3', '4', '5'
                                  '6', '7', '8', '9', '0']

    operator = ['+', '-']

    def isFloat(self, s):
        dot_count = 0
        for i, num in enumerate(s):
            if i == 0:
                if num not in self.number and num not in self.operator:
                    return False
            else:
                if num not in self.number:
                    if num == "." and dot_count == 0:
                        dot_count += 1
                    else:
                        return False
        return True

    def isInt(self, s):
        for i, num in enumerate(s):
            if i == 0:
                if num not in self.number and num not in self.operator:
                    return False
            else:
                if num not in self.number:
                    return False
        return True

if __name__ == '__main__':
    a = "123.45e+6"
    s = Solution()
    s.isNumeric(a)