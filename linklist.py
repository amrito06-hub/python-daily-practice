# Singly Linked List Implementation in Python

class Node:
    """Class to represent a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node


class LinkedList:
    """Class to represent the linked list."""
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def remove(self, data):
        """Remove the first occurrence of a node with the given data."""
        if not self.head:
            print("The linked list is empty. Cannot remove element.")
            return

        # If the node to be removed is the head
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Bypass the node to be removed
                return
            current = current.next

        print(f"Element {data} not found in the linked list.")

    def append(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display all elements in the linked list."""
        if not self.head:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    try:
        ll = LinkedList()

        # Adding elements to the linked list
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.append(100)
        # Display the linked list
        print("Linked List contents:")
        ll.display()

        ll.remove(30)
        ll.display()

    except Exception as e:
        print(f"An error occurred: {e}")
