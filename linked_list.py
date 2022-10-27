# Linked-List

# Node class
class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

# Linked_list class
class linked_list:
    def __init__(self):
        self.first = None

    # Check if the list hasn't any node
    def is_empty(self):
        return self.first == None

    # Add node at the beginning of the list
    def add_first(self, value):
        self.first = node(value=value, next=self.first)

    # Add node in the end of the list
    def add_next(self, value):
        if not self.first:
            self.first = node(value=value)
            return
        curr = self.first
        while curr.next:
            curr = curr.next
        curr.next = node(value=value)

    # Delete a node
    def delete_node(self, key):
        curr = self.first
        prev = None
        while curr and curr.value != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.first = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Get last node of the list
    def get_last_node(self):
        temp = self.first
        while(temp.next is not None):
            temp = temp.next
        return temp.value

    # Print list
    def print_list( self , separator = " => "):
        node = self.first
        while node != None:
            print(node.value, end = separator)
            node = node.next
