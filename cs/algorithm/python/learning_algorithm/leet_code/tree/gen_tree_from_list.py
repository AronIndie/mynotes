

class Tree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def gen_tree(arr) -> Tree:

    for i in range(len(arr) // 2 - 1, -1, -1):
        k = 2 * i + 1
        arr[i] = Tree(arr[i])
        while k < len(arr):
            if not isinstance(arr[k], Tree):
                arr[k] = Tree(arr[k])
            arr[i].left = arr[k]
            if k + 1 < len(arr):
                if not isinstance(arr[k + 1], Tree):
                    arr[k + 1] = Tree(arr[k + 1])
                arr[i].right = arr[k+1]
            i = k
            k = 2 * k + 1
    return arr[0]

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    gen_tree(a)
