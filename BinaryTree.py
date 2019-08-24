class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data  <= self.data:
                if self.left is None:
                    newNode = Node(data)
                    self.left = newNode
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    newNode = Node(data)
                    self.right = newNode
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()
        