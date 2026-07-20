


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def show_all(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                print(f"{value} is in list")
                return
            current = current.next
        print(f"{value} is not in list")

    def remove(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"{value} was not found")

    def change(self, old_value, new_value):
        current = self.head
        while current is not None:
            if current.value == old_value:
                current.value = new_value
                print(f"{old_value} has been changed to {new_value}")
                return
            current = current.next
        print(f"{old_value} was not found")

def main_menu():
    print(""
          "\n1 to add"
          "\n2 to remove"
          "\n3 show all"
          "\n4 check if value presented in the list"
          "\n5 change existing value"
          "\n6 exit")


linked_list = LinkedList()
while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == "6":
        break
    elif choice == "1":
        linked_list.add(int(input("Enter value to be added: ")))
    elif choice == "2":
        linked_list.remove(int(input("Enter value to be removed: ")))
    elif choice == "3":
        linked_list.show_all()
    elif choice == "4":
        linked_list.contains(int(input("Enter value to be checked: ")))
    elif choice == "5":
        try:
            old_value, new_value = map(
                int,
                input("Enter old and new value separated by space: ").split()
            )
            linked_list.change(old_value, new_value)
        except ValueError:
            print("Please enter exactly two integer values separated by space.")

    else:
        print("Invalid choice")








