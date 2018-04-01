# -*- coding:utf-8 -*-

dic = {
    1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",
    16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"
}

def transfer(a: int) -> str:
    if a <= 26:
        return dic[a]
    length = 1
    s = 26
    before = -1
    while s < a:
        length += 1
        s += 26**length
        before += 26**(length - 2)

    s = s - 26**length
    s = a - s
    left = before + s // 26 + 1
    if s % 26 == 0:
        right = 26
        left -= 1
    else:
        right = s % 26

    return transfer(left) + dic[right]

def transfer2(b: str) -> int:
    dic2 = {j:i for i, j in dic.items()}
    s = 0
    for i in range(len(b)):
        s += 26**(len(b) - 1 - i) * dic2[b[i]]
    return s


if __name__ == '__main__':
    print(transfer(26 + 26*26))
    print(transfer2("BC"))

