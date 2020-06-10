"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None        

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left: 
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while len(queue) > 0:
            val = queue.dequeue()
            print(val.value)
            if val.left:
                queue.enqueue(val.left)
            if val.right:
                queue.enqueue(val.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while len(stack) > 0:
            val =stack.pop()
            print(val.value)
            if val.left:
                stack.push(val.left)
            if val.right:
                stack.push(val.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node=None):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

class Queue:
        def __init__(self):
            self.size = 0
            self.storage = LinkedList()
        
        def __len__(self):
            return self.size

        def enqueue(self, value):
            self.size += 1
            self.storage.add_to_head(value)

        def dequeue(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.remove_tail()

class Stack:
        def __init__(self):
            self.size = 0
            self.storage = LinkedList()

        def __len__(self):
            return self.size

        def push(self, value):
            self.size += 1
            self.storage.add_to_tail(value)

        def pop(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.remove_tail()

class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next_node = next

        def get_value(self):
            return self.value

        def get_next(self):
            return self.next_node

        def set_next(self, new_next):
            self.next_node = new_next

class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def add_to_tail(self, data):
            new_node = Node(data)

            if not self.head and not self.tail:
                self.head = new_node
                self.tail = new_node

            else:
                self.tail.set_next(new_node)
                self.tail = new_node
        
        def add_to_head(self, value):
            newNode = Node(value)

            if not self.head and not self.tail:
                self.head = newNode
                self.tail = newNode

            else:
                newNode.set_next(self.head)
                self.head = newNode

        def remove_tail(self):
            if self.tail is None:
                return None
            
            data = self.tail.get_value()
            
            if self.head is self.tail:
                self.head = None
                self.tail = None
            
            else:
                current = self.head
                while current.get_next() != self.tail:
                    current = current.get_next()
                self.tail = None
                self.tail = current
            
            return data

        def remove_head(self):
            if self.head is None:
                return None
            
            data = self.head.get_value()
            
            if self.head is self.tail:
                self.head = None
                self.tail = None
        
            else:
                self.head = self.head.get_next()

            return data

        def contains(self, data):
            if not self.head:
                return False

            current = self.head 

            while current is not None:
                if current.get_value() == data:
                    return True

                current = current.get_next()
            
            return False

        def get_max(self):
            if self.head is None:
                return None

            max_so_far = self.head.get_value()

            current = self.head.get_next()

            while current is not None:
                if current.get_value() > max_so_far:
                    max_so_far = current.get_value()

                current = current.get_next()
                
            return max_so_far