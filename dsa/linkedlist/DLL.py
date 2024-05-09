class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insertAtHead(self, data):
        newnode = Node(data)

        if not self.head:
            self.head = newnode
            return

        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
        return

    def arraytoDll(self, arr):
        newnode = Node(arr[0])
        head = newnode
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            newnode.next = temp
            temp.prev = newnode
            newnode = temp
        

        while head:
            print(head.data ,'', end='')
            head = head.next



    def println(self):
        temp = self.head
        print('Null', end='')
        while temp:
            print(' <- ', end='')
            print(temp.data, end='')
            print(' -> ', end='')
            temp = temp.next
        print('Null')



ll = LinkedList()
ll.insertAtHead(30)
ll.insertAtHead(20)
ll.insertAtHead(10)
ll.println()
ll.arraytoDll([10, 20, 30])
