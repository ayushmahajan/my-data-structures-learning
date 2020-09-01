class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self._head = None

    def insertAtBeginning(self, data):
        # create a new node
        new_node = Node(data)

        # check if the list is empty
        if self._head is None:
            self._head = new_node
            return

        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node

    def printList(self):
        print("Printing List...")
        current = self._head
        while current:
            print(current.data)
            current = current.next

    def printListReverse(self):
        if self._head is None:
            return

        print("Printing List in reverse...")
        current = self._head
        while current.next:
            current = current.next

        while current:
            print(current.data)
            current = current.prev


if __name__ == "__main__":
    dllist = DLL()
    for i in range(1, 6):
        dllist.insertAtBeginning(i)
    dllist.printList() # 5 4 3 2 1
    dllist.printListReverse() # 1 2 3 4 5
