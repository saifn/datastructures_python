class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        #This is the reference variable used to point to the first node of the list.
        self.start = None

    def create_list(self):
        pass

    def display_list(self):
        if(self.start == None):
            print("The list is empty")
            return
        else:
            print("The List is:")
            p = self.start
            while p is not None:
                print("P info is", p.info)
                p = p.next
            print()

    def count_nodes(self):
        if(self.start == None):
            print("The list is empty")
            return
        else:
            n = 0
            p = self.start
            while p is not None:
                n+=1
                p = p.next

            print("The number of nodes in the LL is = ", n)

    def search(self,x):
        if(self.start == None):
            print("The list is empty\n")
            return
        else:
            p = self.start
            position = 0

            while p is not None:
                if(p.info == x):
                    print(x, "is found at position = ", position+1)
                    return True
                else:
                    p = p.next
                    position += 1
            else:
                print("The number is not found in the list")
                return False

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start

        #Careful here if you do p is not None: Then you will have no p.next to insert temp into
        #p.next is None means you can assign temp to p.next since it is none.
        #Error you would get: AttributeError: 'NoneType' object has no attribute 'next'

        while p.next is not None:
            p = p.next

        p.next = temp

    def create_list(self):
        n = int(input("Enter the number of nodes in the list: "))

        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)

    # Important Method: Reversing a Singly Linked List.
    # you need three pointers - prev, p (current) and next

    def reverse_linked_list(self):
        #initialize prev to None and p to the start Node.
        prev = None
        p = self.start
        #Loop through as long as you do not reach the last Node.
        while p is not None:
            #next pointer will point the next node of P. This is only to keep a reference
            #for later because the link is broken in the next statement.
            next = p.next
            #break the next pointer link and point to previous. Here the link is broken to next.
            p.next = prev
            #previous now moves to p's location.
            prev = p
            #Keeping a reference to next helps move p to the next node and the loop continues
            p = next

        #once the list has been reversed you change the reference pointer
        self.start = prev


list = SinglyLinkedList()

list.create_list()

while True:
    print("1. Display List")
    print("2. Count the number of nodes")
    print("3. Search for an element in the List")

    option = int(input("Enter your choice of element: "))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        number = int(input("Enter the number you want to search for?"))
        list.search(number)
