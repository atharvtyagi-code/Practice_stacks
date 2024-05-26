class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self):
        num = int(input("How many datas in the list: "))

        for i in range(num):
            n = input("Add a data in the list: ")
            self.queue.append(n)

        print(self.queue)

    def dequeue(self):
        if len(self.queue) == 0:
            print("There is nothing to remove from the list!")

        else:
            self.queue.pop(0)
            print(self.queue)

    def peek(self):
        if len(self.queue) == 0:
            print("There is nothing to print.")

        else:
            print(self.queue[0])

    def isEmpty(self):
        if len(self.queue) == 0:
            print("It's empty!")

        else:
            print("It's full!")

    def size(self):
        print(len(self.queue))

    def front(self):
        if len(self.queue) == 0:
            print("There is nothing in the list!")

        else:
            print(self.queue[0])

    def rear(self):
        if len(self.queue) == 0:
            print("There is nothing in the list!")

        else:
            print(self.queue[-1])


queues = Queue()
queues.enqueue()
queues.dequeue()
queues.peek()
queues.isEmpty()
queues.size()
queues.front()
queues.rear()