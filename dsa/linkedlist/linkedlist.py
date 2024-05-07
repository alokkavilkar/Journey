# class for Node type data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def addAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
            return
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, '->', end="")
            temp = temp.next
        
        print('Null')
        

myList = Linkedlist()
myList.addAtHead(10)
myList.addAtHead(20)
myList.addAtHead(30)
myList.printList()
