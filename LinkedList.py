class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval 
    
    def insertAtBeginning(self, data):
        newNode  =  Node(data)
        newNode.nextval = self.headval
        self.headval = newNode

l =  SLinkedList()
l.headval = Node("Mon")

e1 = Node("Tue")
e2 = Node("wed")

l.headval.nextval = e1
e1.nextval  = e2

l.listprint()

l.insertAtBeginning("hello world")

l.listprint()
