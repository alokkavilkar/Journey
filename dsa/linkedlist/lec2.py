class Employee:
    company = "Google"

    def getSalary(self):
        print("Salary is 100k", self.name, self.company)

    @classmethod
    def greet(cls, name):
        print("Good moring sir", cls.company, name)

    @staticmethod
    def printsalary(salary):
        print('{:,.2f}'.format(salary))

    


alok = Employee()
alok.name = 'alok'
alok.getSalary()
mahesh = Employee()
# mahesh.getSalary()
alok.greet('aloki')
alok.printsalary(2000)

# alok.getSalary() => Employee.getSalary(alok)


class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

class Linkedlist:

    def addAtHead(self, head,  data):
        newNode = Node(data)
        if head is None:
            head = newNode
            return head
        
        newNode.nxt = head
        head = newNode
        return head

    def printlist(self,head):
        temp = head
        while temp:
            print(temp.data , ' -> ', end='')
            temp = temp.nxt

        print('Null')
        

head = Node(10)
list2 = Linkedlist()
newhead = list2.addAtHead(head, 20)
newhead = list2.addAtHead(newhead, 30)
list2.printlist(newhead)


print('{:.2f}'.format(1000))
# : specifies that formatting starts now.

print('{:,.2f}'.format(1000))

print('{:,d}'.format(1000000))

print('{:s}'.format('HelloWorld'))

print('{:.2%}'.format(0.75))
