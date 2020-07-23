class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return ("No element in the Stack")


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
print(AStack.remove())
print(AStack.remove())
print(AStack.remove())
