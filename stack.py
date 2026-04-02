class ArrayStack:

    def __init__(self):
        # this list is where all the items live
        # starts empty when we create a new stack
        self.items = []

    def push(self, item):
        # add a new item to the top of the stack
        self.items.append(item)

    def pop(self):
        # remove the top item and return it
        # if the stack is empty we cannot pop anything so raise an error
        if self.is_empty():
            raise Exception("The stack is empty, cannot pop")
        return self.items.pop()

    def peek(self):
        # look at the top item without removing it
        # raise an error if there is nothing in the stack
        if self.is_empty():
            raise Exception("The stack is empty, cannot peek")
        # -1 gives us the last item in the list which is the top
        return self.items[-1]

    def is_empty(self):
        # returns True if there is nothing in the stack, False if there is
        if len(self.items) == 0:
            return True
        return False

    def clear(self):
        # wipe out everything in the stack
        self.items = []

    def size(self):
        # returns how many items are currently in the stack
        return len(self.items)
