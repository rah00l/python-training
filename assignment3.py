
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

2. Write a Python program to create a class representing a linked list data structure. 
	Include methods for displaying linked list data, inserting and deleting nodes.

# :: Solution ::

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return

        # If head needs to be removed
        if self.head.data == data:
            self.head = self.head.next
            return

        # Find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print(f"Node with data {data} not found.")


# Example usage:
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.display()  # 1 -> 2 -> 3 -> None
ll.delete(2)
ll.display()  # 1 -> 3 -> None
ll.delete(4)  # Node with data 4 not found.

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

3. Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price.


# :: Solution ::

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity}
        print(f'Added {quantity} of {item_name} to cart.')

    def remove_item(self, item_name):
        if item_name in self.cart:
            del self.cart[item_name]
            print(f'Removed {item_name} from cart.')
        else:
            print(f'{item_name} is not in the cart.')

    def total_price(self):
        total = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return total

    def display_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for item, details in self.cart.items():
                print(f"{item}: {details['quantity']} @ ${details['price']} each")


# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 1.5, 3)
cart.add_item("Banana", 0.75, 5)
cart.display_cart()
print(f"Total price: ${cart.total_price():.2f}")  # Total price: $8.25
cart.remove_item("Banana")
cart.display_cart()


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

4. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
