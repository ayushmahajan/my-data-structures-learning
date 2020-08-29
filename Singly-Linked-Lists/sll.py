class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def insertAtBeginning(self, data):
        # create a new Node
        new_node = Node(data)

        # When the list is empty the head equals to None.
        # So, we can simply have a single statement to handle the
        # empty list and the non-empty list case.

        new_node.next = self._head
        self._head = new_node

    def printList(self):
        temp = self._head
        while temp:
            print(temp.data)
            temp = temp.next 


if __name__ == "__main__":
    llist = LinkedList()
    llist.insertAtBeginning(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtBeginning(4)
    llist.printList() # 4 -> 3 -> 2 -> 1
