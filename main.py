class Stacks():
    def __init__(self):
        self.stacks = []

    def push(self):
        n = int(input("How many words in the list: "))

        for i in range(n):
            num = str(input("Add a word in the list: "))
            self.stacks.append(num)

        print(self.stacks)

    def pop(self):
        self.stacks.pop()
        print(self.stacks)

    def peek(self):
        print(self.stacks[-1])

    def isEmpty(self):
        if len(self.stacks) == 0:
            print("It's empty!")

        else:
            print("It's full!")

    def size(self):
        print(len(self.stacks))

stack = Stacks()

stack.push()
stack.pop()
stack.peek()
stack.isEmpty()
stack.size()