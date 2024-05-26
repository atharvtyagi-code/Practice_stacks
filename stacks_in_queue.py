class Stack_Using_Queue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self):
        num = int(input("How many datas in the list: "))

        for i in range(num):
            n = input("Add a data in the list: ")
            self.queue1.append(n)

        print(self.queue1)

    def pop(self):
        if len(self.queue1) == 0:
            print("There is nothing to remove!")

        else:
            self.queue1.pop(-1)
            print(self.queue1)

    def peek(self):
        if len(self.queue1) == 0:
            print("There is nothing to print!")

        else:
            print(self.queue1[-1])

    def isEmpty(self):
        if len(self.queue1) == 0:
            print("It's empty!")

        else:
            print("It's full!")

    def size(self):
        print(len(self.queue1))


stack = Stack_Using_Queue()

stack.push()
stack.pop()
stack.peek()
stack.isEmpty()
stack.size()