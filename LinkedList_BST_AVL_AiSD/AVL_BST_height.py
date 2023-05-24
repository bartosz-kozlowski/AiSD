import random
from statistics import mean
BST_h=[]
AVL_h=[]
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)

    def display(self):
        if self.root is not None:
            self._display(self.root)

    def _display(self, current_node):
        if current_node is not None:
            self._display(current_node.left_child)
            print(current_node.value, end=" ")
            self._display(current_node.right_child)

    def get_height(self):
        if self.root is not None:
            return self._get_height(self.root, 0)
        else:
            return 0

    def _get_height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._get_height(current_node.left_child, current_height + 1)
        right_height = self._get_height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

class AVL(BST):
    def __init__(self):
        super().__init__()
#order
#in
    @staticmethod
    def from_bst(bst):
        values = []
        AVL._in_order_traversal(bst.root, values)
        avl = AVL()
        avl.root = AVL._build_avl_tree(values, 0, len(values) - 1)
        return avl

    @staticmethod
    def _in_order_traversal(current_node, values):
        if current_node is not None:
            AVL._in_order_traversal(current_node.left_child, values)
            values.append(current_node.value)
            AVL._in_order_traversal(current_node.right_child, values)
#

    @staticmethod
    def _build_avl_tree(values, start, end):
        if start > end:
            return None
        middle = (start + end) // 2
        node = Node(values[middle])
        node.left_child = AVL._build_avl_tree(values, start, middle - 1)
        node.right_child = AVL._build_avl_tree(values, middle + 1, end)
        return node


def get_element_heights(bst, avl, element):
    bst_node = bst.root
    bst_height = 0
    while bst_node is not None:
        if bst_node.value == element:
            break
        elif bst_node.value < element:
            bst_node = bst_node.right_child
            bst_height += 1
        else:
            bst_node = bst_node.left_child
            bst_height += 1

    avl_node = avl.root
    avl_height = 0
    while avl_node is not None:
        if avl_node.value == element:
            break
        elif avl_node.value < element:
            avl_node = avl_node.right_child
            avl_height += 1
        else:
            avl_node = avl_node.left_child
            avl_height += 1

    return (bst_height, avl_height)


##print


#normalne
"""
for _ in range(1):
    n=10000
    while n<=150000:
        print("Długość",n)
        for _ in range(25):
            X = random.sample(range(1, 1000001), n)

            bst = BST()
            for i in range(n):
                bst.insert(X[i])

            #print("BST:")
            #bst.display()

            #print("BST height:", bst.get_height())
            BST_h.append(bst.get_height)

            avl = AVL.from_bst(bst)

            # display the AVL tree
            #print("AVL:")
            #avl.display()

           # print("AVL height:", avl.get_height())
            AVL_h.append(avl.get_height)
        avg_avl_height = mean([h() for h in AVL_h])
        avg_bst_height = mean([h() for h in BST_h])
        print("BST",avg_bst_height)
        print("AVG",avg_avl_height)

        # wysokość elementu
        bst_height, avl_height = get_element_heights(bst, avl, 1)

        print("BST height for value:", bst_height)
        print("AVL height for value:", avl_height)
        n+=10000

        print_trees(bst, avl)

"""
#z pliku
with open('test.txt', 'r') as A1:
    for A1 in A1:
        exec(A1)
##^^ odczyt pliku
for _ in range(1):
    n=len(A1)
    print("Długość",n)
    for _ in range(1):
        X = A1

        bst = BST()
        for i in range(n):
            bst.insert(X[i])

        #print("BST:")
        #bst.display()

        #print("BST height:", bst.get_height())
        BST_h.append(bst.get_height)

        avl = AVL.from_bst(bst)

        # display the AVL tree
        #print("AVL:")
        #avl.display()

       # print("AVL height:", avl.get_height())
        AVL_h.append(avl.get_height)
    avg_avl_height = mean([h() for h in AVL_h])
    avg_bst_height = mean([h() for h in BST_h])
    print("BST",avg_bst_height)
    print("AVG",avg_avl_height)

    # wysokość elementu
    bst_height, avl_height = get_element_heights(bst, avl, 10)

    print("BST height for value:", bst_height)
    print("AVL height for value:", avl_height)





