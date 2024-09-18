
Assignment 3:

Assignment- OOP

1. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# :: Solution ::

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(f'Pushed {element} to stack.')

    def pop(self):
        if not self.is_empty():
            element = self.stack.pop()
            print(f'Popped {element} from stack.')
            return element
        else:
            print('Stack is empty!')
            return None

    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
s = Stack()
s.push(10)
s.push(20)
s.pop()  # Popped 20
s.pop()  # Popped 10
s.pop()  # Stack is empty!

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

2. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.

3. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

4. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
