class Node:
    data = 0
    nextNode = None

    def __init__(self, data:int) -> None:
        self.data = data
        self.nextNode = None
        


    
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.nextNode = node2
node2.nextNode = node3

curr_node = node1

while curr_node is not None:

    print(curr_node.data)
    curr_node = curr_node.nextNode




