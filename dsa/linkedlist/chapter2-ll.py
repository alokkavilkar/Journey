class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        newnode.next = self.head
        head = newnode

    def insertAtTail(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return 

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        return
    
    def insertAtK(self, data, k):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        
        # 1  2 3 4 5 k=2 10  => 1 10 2 3 4 5

        if k == 1:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        count = 1
        while temp:
            if count == k - 1:
                nextnode = temp.next
                temp.next = newnode
                newnode.next = nextnode
                return
            temp = temp.next
            count += 1

    'insert at value after or before'
    'before'
    def insertAtValue(self, data, value):
        temp = self.head
        newnode = Node(data)
        if self.head == value:
            self.head = newnode
            return

        while temp.next:
            if temp.next.data == value:
                nodenext = temp.next
                temp.next = newnode
                newnode.next = nodenext
                return

            temp = temp.next



    def printList(self):
        temp = self.head
        while temp:
            print(temp.data , '->', end='')
            temp = temp.next
        
        print('Null')


    def deleteAtHead(self):
        if self.head is None:
            return

        temp = self.head
        self.head = self.head.next
        del temp
        return

    def deleteAtTail(self):
        if self.head is None:
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        tail = temp.next
        temp.next = None
        del tail
        

    def deleteAtK(self, k):

        if k == 1:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        
        temp = self.head
        prev = None
        count = 1
        while temp:
            if count == k:
                temp2 = prev.next
                prev.next = prev.next.next
                del temp2
                return
            prev = temp
            temp = temp.next
            count += 1





        
ll = LinkedList()
ll.insertAtHead(10)
ll.insertAtTail(20)
ll.insertAtTail(30)
ll.insertAtTail(40)
ll.insertAtK(50, 5)
ll.insertAtK(100, 5)
ll.printList()
ll.insertAtValue(10, 20)
ll.printList()
ll.deleteAtHead()
ll.printList()
ll.deleteAtTail()
ll.printList()
ll.deleteAtK(4)
ll.printList()
