"""
In Python the list class already supports the push functionality of the Stack ADT.
We can use the append method to add the element to the end of the list.
Similarly, we can use the pop method to pop the last element from the list.
"""

"""
So, the question arises why create Stack when we have lists?
1. List supports accessing the elements via index and stack doesn't.
2. The terminology of the list class is different from that of Stack.(For instance: append and push)
"""


class Empty(Exception):
    pass


class StackUsingArray:
    def __init__(self):
        # create an empty stack
        self._data = []  # data is a private instance

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()  # Removes and returns the last element of the list

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]  # returns the last element of the list


if __name__ == "__main__":
    stack = StackUsingArray()
    stack.push(5)  # 5
    stack.push(3)  # 3 5
    print(len(stack))  # 2
    print(stack.is_empty())  # False
    print(stack.pop())  # 3
    print(stack.top())  # 5
    print(stack.pop())  # 5
    print(stack.top())  # Exception Raised
