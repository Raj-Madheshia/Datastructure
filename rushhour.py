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
        self.buildTree(list(self.newnode.data))
        
    def buildTree(self, root):
        depth =0
        self.dep = 0
        root = np.array(root).tolist()
        self.expansion=[]
        self.tester = []
        while(self.buildNeeded):
            self.expansion = []
            self.tester = []
            self.makeChildren(root, depth)
            print("DEPTH: ",depth+1)
            self.printTraverse(self.tester)
            depth+=1
            self.dep = depth
            
        
        if  self.buildNeeded == False:
            print("The Path found at Level of----> ", self.dep)
            print("Path of car is :")
            self.printTraverse(self.pathNode)

    def checkForMatrix(self, parent, x,y):
        if parent[x][y] != 0:
            return False
        else:
            return True

    def makeChildren(self, parent, depth):
        if depth>=0:
            self.expansion.append(parent)
            self.tester.append(parent)
        else:
            return

        if self.buildNeeded==False:
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
                            self.tester.append(new)
                        self.pathNode = self.expansion.copy()
                        self.dep+=1
                        self.buildNeeded=False
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
                                self.makeChildren(new,depth-1)
                    newparent = np.array(parent.copy())
                    if y2<(newparent.shape[-1]-1):
                        isPossible = self.checkForMatrix(newparent, x, y2+1)
                        if isPossible:
                            newparent[x][y2+1]=i
                            newparent[x][y1]=0
                            new = np.array(newparent).tolist()
                            if new not in self.expansion:
                                self.makeChildren(new,depth-1)
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
                                self.makeChildren(new,depth-1)

                    newparent = np.array(parent.copy())
                    if x2<(newparent.shape[0]-1):
                        isPossible = self.checkForMatrix(newparent, x2+1, y)
                        if isPossible:
                            newparent[x2+1][y]=i
                            newparent[x1][y]=0
                            new = np.array(newparent).tolist()
                            if new not in self.expansion:
                                self.makeChildren(new,depth-1)
        
        self.expansion.pop()
            
            

    def pathClear(self, parent, x, y):
        chk = 0
        for i in parent[x][y+1:]:
            if i!=0:
                chk =1
        if chk ==0:
            return True
        else:
            return False


    def printTraverse(self, value):
        # count =0
        # for i in self.expansion:
        #     if count%5==0:
        #         print()
        #     print(i, end=" ")
        #     count+1
        
        start = 0
        end = np.array(value).shape[-1]-1
        if end >=len(value):
            new = value[start:len(value)]
            for i in list(zip(*new)):
                print(i)
            print("\n")
        while(end<len(value)):
            new = value[start:end]
            for i in list(zip(*new)):
                print(i)
            print("\n")
            start = end
            end +=5
            if end >=len(value):
                end = len(value)
                new = value[start:len(value)]
                for i in list(zip(*new)):
                    print(i)
                print("\n")


a = np.array([[0,0,0],
              [9,9,2],
              [0,0,2],
              [0,1,1]])

test = RushHour(a)
