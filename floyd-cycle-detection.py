"""
Working of floyd cycle detection
1. make to pointer hare and tortoties and assign them to the start or head
2. move hare by 2 and move tortoties by 1
3. when they meet break the while loop
4. assign the tortoties to start of linked list
5. move both pointer one step and where they meet is the start of cycle

"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.dataval)
            temp = temp.next

    def cyclestart(self):
        self.tot = self.head.next
        self.hare = self.head.next
        if self.hare.next:
            self.hare = self.hare.next
        else:
            print("No cycle is present")
            return
        # print(self.hare.dataval, self.tot.dataval)
        while(self.tot and self.tot!=self.hare):
            self.tot = self.tot.next
            if self.hare.next:
                self.hare = self.hare.next.next
            else:
                print("No cycle is present")
                break
            # print(self.hare.dataval, self.tot.dataval)
        
        if not self.tot:
            print("No cycle is present")
        self.tot = self.head
        while self.tot != self.hare:
            self.tot = self.tot.next
            self.hare = self.hare.next
        print(self.tot.dataval)

        

l =  LinkedList()
l.insert(3)
l.insert(5)
l.insert(1)
l.insert(10)
l.insert(11)
l.insert(12)
l.insert(13)
l.insert(14)
l.insert(15)
l.insert(16)
l.head.next.next.next.next.next.next.next.next.next.next = l.head.next.next.next.next
l.cyclestart()



