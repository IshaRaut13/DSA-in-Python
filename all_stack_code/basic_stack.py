class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        s = self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.display()
print(s.size())

s.pop()
s.display()

print(s.peek())
s.display()
