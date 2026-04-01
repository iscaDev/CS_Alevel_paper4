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
        self.__Tree = [Node(-1, None, None) for i in range(20)] # array of type Node
        self.__FirstNode = -1 # FirstNode as INTEGER
        self.__NumberNodes = 0 # NumberNodes as INTEGER

    def InsertNode(self, NewNode):
        if NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__Tree[self.__FirstNode].GetData()