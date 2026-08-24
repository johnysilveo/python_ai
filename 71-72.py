

def task_one():
    class Stack:
        def __init__(self, max_size):
            self.max_size = max_size
            self.stack = []

        def is_empty(self):
            if len(self.stack) == 0:
                return True
            return False

        def is_full(self):
            if len(self.stack) == self.max_size:
                return True
            return False

        def push(self, value):
            if not self.is_full():
                self.stack.append(value)
            else:
                print("Stack is full")

        def pop(self):
            if not self.is_empty():
                return self.stack.pop()
            else:
                return "Stack is empty"

        def peek(self):
            if not self.is_empty():
                return self.stack[-1]
            else:
                return "Stack is empty"

        def size(self):
            return len(self.stack)

        def clear(self):
            self.stack.clear()
            return "Stack is empty now"

        def limit(self):
            return self.max_size

    stack = Stack(5)

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Size")
        print("4. Is empty")
        print("5. Is full")
        print("6. Clear")
        print("7. Peek")
        print("8. Max size?")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "0":
            break
        elif choice == "1":
            value = input("Enter your entry: ")
            stack.push(value)
        elif choice == "2":
            print(stack.pop())
        elif choice == "3":
            print(f"Stack size is {stack.size()}")
        elif choice == "4":
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is full")
        elif choice == "5":
            if stack.is_full():
                print("Stack is empty")
            else:
                print("Stack isn't empty")
        elif choice == "6":
            stack.clear()
            print("Stack is empty now")
        elif choice == "7":
            print(f"Last element is {stack.peek()}")
        elif choice == "8":
            print(f"Max size is {stack.limit()}")



from datetime import datetime



def task_two():
    class ServerQueue:
        def __init__(self):
            self.queue = []
            self.statistics = []

        def add_client(self, client, priority):
            entry_queue = (client, priority)
            self.queue.append(entry_queue)
            self.queue.sort(key=lambda x: x[1], reverse=True)

        def process_client(self):
            if len(self.queue) > 0:
                entry = self.queue.pop(0)
                client, priority = entry
                entry_stat = (
                    client,
                    datetime.now().strftime("%H:%M:%S")
                )
                self.statistics.append(entry_stat)
                return client
            else:
                return "Queue is empty"

        def show_queue(self):
            if len(self.queue) == 0:
                print("Queue is empty")
            else:
                for client, priority in self.queue:
                    print(f"Client {client} has priority {priority}")

        def show_statistics(self):
            if len(self.statistics) == 0:
                print("Statistics are empty")
            else:
                for client, time in self.statistics:
                    print(f"Client {client} was processed at {time}")

    server = ServerQueue()

    while True:
        print("\n1. Add client")
        print("2. Process client")
        print("3. Show queue")
        print("4. Show statistics")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "0":
            break
        elif choice == "1":
            client = input("Enter a client' name: ")
            priority = int(input("Enter a priority: "))
            server.add_client(client, priority)
        elif choice == "2":
            print(server.process_client())
        elif choice == "3":
            server.show_queue()
        elif choice == "4":
            server.show_statistics()
task_one()
task_two()