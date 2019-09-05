import numpy as np
from collections import Counter
from queue import Queue
from copy import copy
"""
Assuming 9 as a car.
Taken Car size 2 .
This program is Iterative deeping search for finding solution of Rush hour.
The goal for this program is find path for Car(9) to reach at right side.
"""

class Node:
    def __init__(self, new):
        self.parent = None
        self.data = new
    def printdata(self):
        print(self.data)

class RushHour:
    def __init__(self, data):
        self.newnode = Node(data)
        self.buildNeeded = True
        a = self.newnode.data
        a = a.reshape(-1)
        b = Counter(a)
        self.listOfCar = list(b.keys())
        if self.isFinal():
            print("Level: 0")
            print(self.newnode.data)
        else:
            self.buildTree(list(self.newnode.data))
            
    def buildTree(self, root):
        depth =0
        self.dep = 0
        root = np.array(root).tolist()
        self.expansion=[root]
        while(self.buildNeeded):
            print("===========================",self.dep,"==============================")
            self.printTraverse()
            self.expansion = []
            self.expansion.append(root)
            self.makeChildren(root, depth)
            depth+=1
            self.dep = depth
            
        

    def checkForMatrix(self, parent, x,y):
        if parent[x][y] != 0:
            return False
        else:
            return True

    def makeChildren(self, parent, depth):
        if depth>=0 and self.buildNeeded:
            pass
        else:
            return
        

        for i in self.listOfCar:
            if self.buildNeeded == False:
                return
            if i != 0:
                a= np.where(parent==i)
                if i ==9:
                    x =a[0][0]
                    y1 = a[1][0]
                    y2=a[1][1]
                    
                    if self.pathClear(parent,x,y2):
                        parent = np.array(parent)
                        shp = parent.shape
                        parent[x][y2]=0
                        parent[x][y1]=0
                        parent[x][shp[-1]-1]=9
                        parent[x][shp[-1]-2]=9
                        self.buildNeeded = False
                        new = np.array(parent).tolist()
                        if new not in self.expansion:
                            self.expansion.append(new)
                        self.dep+=1
                        print("===========================",self.dep,"==============================")
                        #print("YES CLEAR", parent)
                        self.printTraverse()
                        break
                
                if a[0][0] == a[0][1]:
                    x = a[0][0]
                    y1 = a[1][0]
                    y2 = a[1][1]
                    newparent = np.array(parent.copy())
                    if y1 > 0:   
                        isPossible = self.checkForMatrix(newparent, x, y1-1)
                        if isPossible:
                            newparent[x][y1-1]=i
                            newparent[x][y2]=0
                            #print("Depth Possibile :", self.dep,".....Current: ",depth,newparent)
                            new = np.array(newparent).tolist()
                            if new not in self.expansion:
                                self.expansion.append(new)
                            self.makeChildren(list(newparent),depth-1)
                    newparent = np.array(parent.copy())
                    if y2<(newparent.shape[-1]-1):
                        isPossible = self.checkForMatrix(newparent, x, y2+1)
                        if isPossible:
                            newparent[x][y2+1]=i
                            newparent[x][y1]=0
                            new = np.array(newparent).tolist()
                            if new not in self.expansion:
                                self.expansion.append(new)
                            #print("Depth Possibile :", self.dep,".....Current: ",depth,newparent)
                            self.makeChildren(list(newparent),depth-1)
                    elif i==9 and y2==(newparent.shape[-1]-1):
                        self.buildNeeded = False
                        new = np.array(newparent).tolist()
                        if new not in self.expansion:
                            self.expansion.append(new)
                        #print("Depth Possibile :", self.dep,".....Current: ",depth,newparent)
                        #print(newparent)
                        #self.printTraverse()
                        break
                        
                elif a[1][0] == a[1][1]:
                    y = a[1][0]
                    x1 = a[0][0]
                    x2 = a[0][1]
                    newparent = np.array(parent.copy())
                    if x1 > 0:
                        isPossible = self.checkForMatrix(newparent, x1-1, y)
                        if isPossible:
                            newparent[x1-1][y]=i
                            newparent[x2][y]=0
                            new = np.array(newparent).tolist()
                            if new not in self.expansion:
                                self.expansion.append(new)
                            #print("Depth Possibile :", self.dep,".....Current: ",depth,newparent)
                            self.makeChildren(list(newparent),depth-1)

                    newparent = np.array(parent.copy())
                    if x2<(newparent.shape[0]-1):
                        isPossible = self.checkForMatrix(newparent, x2+1, y)
                        if isPossible:
                            newparent[x2+1][y]=i
                            newparent[x1][y]=0
                            new = np.array(newparent).tolist()
                            if new not in self.expansion:
                                self.expansion.append(new)
                            #print("Depth Possibile :", self.dep,".....Current: ",depth,newparent)
                            self.makeChildren(list(newparent),depth-1)
                
    def pathClear(self, parent, x, y):
        chk = 0
        for i in parent[x][y+1:]:
            if i!=0:
                chk =1
        if chk ==0:
            return True
        else:
            return False


    def printTraverse(self):
        # count =0
        # for i in self.expansion:
        #     if count%5==0:
        #         print()
        #     print(i, end=" ")
        #     count+1
        
        start = 0
        end = np.array(self.expansion).shape[-1]-1
        if end >=len(self.expansion):
            new = self.expansion[start:len(self.expansion)]
            for i in list(zip(*new)):
                print(i)
            print("\n")
        while(end<len(self.expansion)):
            new = self.expansion[start:end]
            for i in list(zip(*new)):
                print(i)
            print("\n")
            start = end
            end +=5
            if end >=len(self.expansion):
                end = len(self.expansion)
                new = self.expansion[start:len(self.expansion)]
                for i in list(zip(*new)):
                    print(i)
                print("\n")

    def isFinal(self):
        # write chceking list logic here

        return False

a = np.array([[0,0,0],
              [9,9,1],
              [0,0,1],
              [0,2,2]])

test = RushHour(a)
