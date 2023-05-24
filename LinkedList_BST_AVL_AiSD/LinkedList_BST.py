import random
import timeit
import copy
import numpy as np
L_ins=[]
L_search=[]
L_delete=[]
BST_ins=[]
BST_search=[]
BST_delete=[]
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insertion(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        if temp.data > data:
            new_node.next = temp
            self.head = new_node
            return
        while temp.next:
            if temp.next.data > data:
                break
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def search(self, data):
        current = self.head
        while current is not None and current.data != data:
            current = current.next
        if current is None:
            return False
        else:
            return True

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next
        if current.next is None:
            return
        current.next = current.next.next

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def appendd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def display(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=' -> ')
            curr_node = curr_node.next
        print('None')

    ###############
    def delete_element(self, data):
        start_time = timeit.default_timer()

        if self.head is None:
            end_time = timeit.default_timer()
            return end_time - start_time
        if self.head.data == data:
            self.head = self.head.next
            end_time = timeit.default_timer()
            return end_time - start_time
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next
        if current.next is None:
            end_time = timeit.default_timer()
            return end_time - start_time
        current.next = current.next.next
        end_time = timeit.default_timer()
        return end_time - start_time

class NodeB:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, node, key):
        if node is None:
            return NodeB(key)
        elif key < node.val:
            node.left = self._insert_helper(node.left, key)
        else:
            node.right = self._insert_helper(node.right, key)
        return node

    def search(self, key):
        return self._search_helper(self.root, key)

    def _search_helper(self, node, key):
        if node is None or node.val == key:
            return node
        elif key < node.val:
            return self._search_helper(node.left, key)
        else:
            return self._search_helper(node.right, key)


    def postorder_delete(self, node):
        if node is not None:
            self.postorder_delete(node.left)
            self.postorder_delete(node.right)
            node.left = None
            node.right = None
            node.val = None

    def delete_all(self):
        self.postorder_delete(self.root)
        self.root = None

    #####new del
    def delete(self, key):
        start_time = timeit.default_timer()
        self.root = self._delete_helper(self.root, key)
        end_time = timeit.default_timer()
        return end_time - start_time

    def _delete_helper(self, node, key):
        if node is None:
            return node
        elif key < node.val:
            node.left = self._delete_helper(node.left, key)
        elif key > node.val:
            node.right = self._delete_helper(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.val = temp.val
                node.right = self._delete_helper(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
################################
    def display_inorder(self, node):
        if node is not None:
            self.display_inorder(node.left)
            print(node.val, end=' ')
            self.display_inorder(node.right)

    def display(self):
        self.display_inorder(self.root)
        print()


def search_list_and_tree(linked_list, binary_search_tree, element):
    start_time = timeit.default_timer()
    found_in_list = linked_list.search(element)
    end_time = timeit.default_timer()
    time_list = end_time - start_time

    start_time = timeit.default_timer()
    found_in_tree = binary_search_tree.search(element)
    end_time = timeit.default_timer()
    time_tree = end_time - start_time

    if found_in_list and found_in_tree:
        print("Element", element, "found in both linked list and binary search tree.")
    elif found_in_list:
        print("Element", element, "found in linked list only.")
    elif found_in_tree:
        print("Element", element, "found in binary search tree only.")
    else:
        print("Element", element, "not found in linked list or binary search tree.")

    return time_list, time_tree

#####

def get_min_max(linked_list, binary_search_tree):
    # get minimum value from linked list
    start_time = timeit.default_timer()
    min_list = linked_list.head.data
    end_time = timeit.default_timer()
    time_min_list = end_time - start_time

    # get maximum value from linked list
    start_time = timeit.default_timer()
    curr_node = linked_list.head
    while curr_node.next is not None:
        curr_node = curr_node.next
    max_list = curr_node.data
    end_time = timeit.default_timer()
    time_max_list = end_time - start_time

    # get minimum value from binary search tree
    start_time = timeit.default_timer()
    curr_node = binary_search_tree.root
    while curr_node.left is not None:
        curr_node = curr_node.left
    min_bst = curr_node.val
    end_time = timeit.default_timer()
    time_min_bst = end_time - start_time

    # get maximum value from binary search tree
    start_time = timeit.default_timer()
    curr_node = binary_search_tree.root
    while curr_node.right is not None:
        curr_node = curr_node.right
    max_bst = curr_node.val
    end_time = timeit.default_timer()
    time_max_bst = end_time - start_time

    return min_list, max_list, time_min_list, time_max_list, min_bst, max_bst, time_min_bst, time_max_bst

##### del


#normalne

n = 2000 #'liczba elementow na start'
while n<= 30000:
    print("Długość",n)
    for i in range(5):
        X = random.sample(range(1, 1000001), n)
        Y = copy.deepcopy(X)
        Z = copy.deepcopy(X)
        A = copy.deepcopy(X)
        B = copy.deepcopy(X)

        'wstawianie elementow (i sortowanie ich)'
        linked_list = SortedLinkedList()
        start_time = timeit.default_timer()
        for i in range(n):
            linked_list.insertion(X[i])
        end_time = timeit.default_timer()
        a = end_time - start_time
        L_ins.append(a)
        #print("Czas wstawiania elementów do listy: {:.20f} sekund".format(end_time - start_time))

        'przeszukiwanie'
        start_time = timeit.default_timer()
        for i in range(n):
            linked_list.search(A[i])
        end_time = timeit.default_timer()
        b = end_time - start_time
        L_search.append(b)
        #print("Czas przeszukiwania elementów z listy: {:.20f} sekund".format(end_time - start_time))

        'samo wstawianie elementow, ale bez ich sortowania'
        linkedlist = SortedLinkedList()
        #start_time = timeit.default_timer()
        for i in range(n):
            linkedlist.appendd(Z[i])
        # end_time = timeit.default_timer()
        # print("Czas przeszukiwania elementów z listy: {:.20f} sekund".format(end_time - start_time))

        'usuwanie elementow listy'
        start_time = timeit.default_timer()
        for i in range(n):
            linkedlist.delete_first()
        end_time = timeit.default_timer()
        c = end_time - start_time
        L_delete.append(c)
        #print("Czas usuwania elementów z listy: {:.20f} sekund".format(end_time - start_time))


        'wstawianie elementow do BST'
        bst = BST()
        start_time = timeit.default_timer()
        for i in range(n):
            bst.insert(Y[i])
        end_time = timeit.default_timer()
        d = end_time - start_time
        BST_ins.append(d)
        #print("Czas wstawiania elementów do BST: {:.20f} sekund".format(end_time - start_time))

        #bst.display()
        'szukanie elementow w BST'
        start_time = timeit.default_timer()
        for i in range(n):
            bst.search(B[i])
        end_time = timeit.default_timer()
        e = end_time - start_time
        BST_search.append(e)
        #print("Czas przeszukiwania BST: {:.20f} sekund".format(end_time - start_time))

        'usuwanie BST'
        start_time = timeit.default_timer()
        bst.delete_all()
        end_time = timeit.default_timer()

        f = end_time - start_time
        BST_delete.append(f)
       #print("Czas usuwania elementów z BST: {:.20f} sekund".format(end_time - start_time))

    średnia_IS_ins = np.mean(L_ins)
    print("Linked list insertion", format(średnia_IS_ins, '.20f'))
    L_ins = []

    średnia_IS_search = np.mean(L_search)
    print("Linked list search", format(średnia_IS_search, '.20f'))
    L_search = []

    średnia_IS_delete = np.mean(L_delete)
    print("Linked list delete", format(średnia_IS_delete, '.20f'))
    L_ins = []

    średnia_BST_ins = np.mean(BST_ins)
    print("BST insertion", format(średnia_BST_ins, '.20f'))
    BST_ins = []

    średnia_BST_search = np.mean(BST_search)
    print("BST search", format(średnia_BST_search, '.20f'))
    BST_search = []

    średnia_BST_delete = np.mean(BST_delete)
    print("BST delete", format(średnia_BST_delete, '.20f'))
    BST_ins = []

####szukanie
    # create a linked list and binary search tree
    linked_list = SortedLinkedList()
    binary_search_tree = BST()

    # insert elements into both objects
    for i in range(n):
        linked_list.insertion(X[i])
        binary_search_tree.insert(X[i])

    # search for an element and measure time taken
    element = 10
    time_list, time_tree = search_list_and_tree(linked_list, binary_search_tree, element)

    # print times taken for each search
    print("Time taken to search linked list:", time_list)
    print("Time taken to search binary search tree:", time_tree)


####minmax
    # Call the function to measure the time taken to find the min and max values
    min_list, max_list, time_min_list, time_max_list, min_bst, max_bst, time_min_bst, time_max_bst = get_min_max(linked_list, binary_search_tree)
    list_time=time_min_list+time_max_list
    tree_time=time_min_bst+time_max_bst
    # Print the results
    print(f"Minimum value in list: {min_list}")
    print(f"Maximum value in list: {max_list}")
    print(f"Time taken to find min and max in list: {list_time} seconds")
    print(f"Time taken to find min and max in tree: {tree_time} seconds")

###del
    time_delete = linked_list.delete_element(876)
    print("Time to delete an element from linked list:", time_delete)

    time_taken = bst.delete(3)
    print(f"Time taken to dlete from BST: {time_taken} seconds")
    n+=2000



"""


#z pliku
with open('test.txt', 'r') as A1:
    for A1 in A1:
        exec(A1)
n = len(A1) #'liczba elementow na start'
print("Długość",n)
for i in range(1):
    X = A1
    Y = copy.deepcopy(X)
    Z = copy.deepcopy(X)
    A = copy.deepcopy(X)
    B = copy.deepcopy(X)

    'wstawianie elementow (i sortowanie ich)'
    linked_list = SortedLinkedList()
    start_time = timeit.default_timer()
    for i in range(n):
        linked_list.insertion(X[i])
    end_time = timeit.default_timer()
    a = end_time - start_time
    L_ins.append(a)
    #print("Czas wstawiania elementów do listy: {:.20f} sekund".format(end_time - start_time))

    'przeszukiwanie'
    start_time = timeit.default_timer()
    for i in range(n):
        linked_list.search(A[i])
    end_time = timeit.default_timer()
    b = end_time - start_time
    L_search.append(b)
    #print("Czas przeszukiwania elementów z listy: {:.20f} sekund".format(end_time - start_time))

    'samo wstawianie elementow, ale bez ich sortowania'
    linkedlist = SortedLinkedList()
    #start_time = timeit.default_timer()
    for i in range(n):
        linkedlist.appendd(Z[i])
    # end_time = timeit.default_timer()
    # print("Czas przeszukiwania elementów z listy: {:.20f} sekund".format(end_time - start_time))

    'usuwanie elementow listy'
    start_time = timeit.default_timer()
    for i in range(n):
        linkedlist.delete_first()
    end_time = timeit.default_timer()
    c = end_time - start_time
    L_delete.append(c)
    #print("Czas usuwania elementów z listy: {:.20f} sekund".format(end_time - start_time))


    'wstawianie elementow do BST'
    bst = BST()
    start_time = timeit.default_timer()
    for i in range(n):
        bst.insert(Y[i])
    end_time = timeit.default_timer()
    d = end_time - start_time
    BST_ins.append(d)
    #print("Czas wstawiania elementów do BST: {:.20f} sekund".format(end_time - start_time))

    #bst.display()
    'szukanie elementow w BST'
    start_time = timeit.default_timer()
    for i in range(n):
        bst.search(B[i])
    end_time = timeit.default_timer()
    e = end_time - start_time
    BST_search.append(e)
    #print("Czas przeszukiwania BST: {:.20f} sekund".format(end_time - start_time))

    'usuwanie BST'
    start_time = timeit.default_timer()
    bst.delete_all()
    end_time = timeit.default_timer()

    f = end_time - start_time
    BST_delete.append(f)
   #print("Czas usuwania elementów z BST: {:.20f} sekund".format(end_time - start_time))

    średnia_IS_ins = np.mean(L_ins)
    print("Linked list insertion", format(średnia_IS_ins, '.20f'))
    L_ins = []

    średnia_IS_search = np.mean(L_search)
    print("Linked list search", format(średnia_IS_search, '.20f'))
    L_search = []

    średnia_IS_delete = np.mean(L_delete)
    print("Linked list delete", format(średnia_IS_delete, '.20f'))
    L_ins = []

    średnia_BST_ins = np.mean(BST_ins)
    print("BST insertion", format(średnia_BST_ins, '.20f'))
    BST_ins = []

    średnia_BST_search = np.mean(BST_search)
    print("BST search", format(średnia_BST_search, '.20f'))
    BST_search = []

    średnia_BST_delete = np.mean(BST_delete)
    print("BST delete", format(średnia_BST_delete, '.20f'))
    BST_ins = []


#



# create a linked list and binary search tree
linked_list = SortedLinkedList()
binary_search_tree = BST()

# insert elements into both objects
for i in range(n):
    linked_list.insertion(X[i])
    binary_search_tree.insert(X[i])

# search for an element and measure time taken
element = 10
time_list, time_tree = search_list_and_tree(linked_list, binary_search_tree, element)

# print times taken for each search
print("Time taken to search linked list:", time_list)
print("Time taken to search binary search tree:", time_tree)

####minmax
# Call the function to measure the time taken to find the min and max values
min_list, max_list, time_min_list, time_max_list, min_bst, max_bst, time_min_bst, time_max_bst = get_min_max(linked_list, binary_search_tree)
list_time=time_min_list+time_max_list
tree_time=time_min_bst+time_max_bst
# Print the results
print(f"Minimum value in list: {min_list}")
print(f"Maximum value in list: {max_list}")
print(f"Time taken to find min and max in list: {list_time} seconds")
print(f"Time taken to find min and max in tree: {tree_time} seconds")

###del
time_delete = linked_list.delete_element(876)
print("Time to delete an element from linked list:", time_delete)
time_taken = bst.delete(3)
print(f"Time taken to dlete from BST: {time_taken} seconds")

"""