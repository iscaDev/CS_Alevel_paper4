class Node:
    def __init__(self, dataP, leftP, rightP):
        self.__Data = dataP # Data as INTEGER
        self.__LeftPointer = leftP # LeftPointer as INTEGER
        self.__RightPointer = rightP # RightPointer as INTEGER

    def GetData(self):
        return self.__Data
    def GetLeftPointer(self):
        return self.__LeftPointer
    def GetRightPointer(self):
        return self.__RightPointer

    def SetData(self, dataP):
        self.__Data = dataP
    def SetLeft(self, leftP):
        self.__LeftPointer = leftP
    def SetRight(self, rightP):
        self.__RightPointer = rightP

class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1, -1, -1) for i in range(20)] # array of type Node
        self.__FirstNode = -1 # FirstNode as INTEGER
        self.__NumberNodes = 0 # NumberNodes as INTEGER

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            NodeAccess = self.__FirstNode
            direction = ""
            previous = None
            while NodeAccess != -1:
                previous = NodeAccess
                if NewNode.GetData() < self.__Tree[NodeAccess].GetData():
                    NodeAccess = self.__Tree[NodeAccess].GetLeftPointer()
                    direction = "Left"
                else:
                    NodeAccess = self.__Tree[NodeAccess].GetRightPointer()
                    direction = "Right"
            if direction == "Left":
                self.__Tree[previous].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[previous].SetRight(self.__NumberNodes)

            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(self.__NumberNodes):
                print(self.__Tree[i].GetLeftPointer(), self.__Tree[i].GetData(), self.__Tree[i].GetRightPointer())


# main program
TheTree = TreeClass()
TheTree.InsertNode(Node(10, -1, -1))
TheTree.InsertNode(Node(11, -1, -1))
TheTree.InsertNode(Node(5, -1, -1))
TheTree.InsertNode(Node(1, -1, -1))
TheTree.InsertNode(Node(20, -1, -1))
TheTree.InsertNode(Node(7, -1, -1))
TheTree.InsertNode(Node(15, -1, -1))
TheTree.OutputTree()