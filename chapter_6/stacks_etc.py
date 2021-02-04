class Empty(Exception):
    """ Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """ LIFO stack implementation using a list"""

    def __init__(self):
        self._data = []

    def __len__(self):
        """ Return the length """
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("stach is empty")
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


stack = ArrayStack()
stack.push(20)

print(len(stack))