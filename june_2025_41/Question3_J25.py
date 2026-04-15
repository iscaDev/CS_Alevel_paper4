class Node:
    def __init__(self, dataP):
        self.__NodeData = dataP # NodeData as Integer
        self.__LeftNode = None # LeftNode as Node type
        self.__RightNode = None # RightNode as Node type

    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode
    def GetData(self):
        return self.__NodeData

    def SetLeft(self, dataP):
        self.__LeftNode = dataP
    def SetRight(self, dataP):
        self.__RightNode = dataP

class Tree:
    def __init__(self, firstP):
        self.__FirstNode = firstP # FirstNode as Node type
    def GetRootNode(self):
        return self.__FirstNode
    def Insert(self, nodeP):
        currentNode = self.__FirstNode
        flag = True
        while flag:
            if nodeP.GetData() < currentNode.GetData():
                if currentNode.GetLeft() is None:
                    currentNode.SetLeft(nodeP)
                    flag = False
                else:
                    currentNode = currentNode.GetLeft()
            else:
                if currentNode.GetRight() is None:
                    currentNode.SetRight(nodeP)
                    flag = False
                else:
                    currentNode = currentNode.GetRight()

def OutputInOrder(nodeP):
    if nodeP.GetLeft() is not None:
        OutputInOrder(nodeP.GetLeft())
    print(nodeP.GetData())
    if nodeP.GetRight() is not None:
        OutputInOrder(nodeP.GetRight())


# main program
node1 = Node(10)
node2 = Node(20)
node3 = Node(5)
node4 = Node(15)
node5 = Node(7)
tree = Tree(node1)
tree.Insert(node2)
tree.Insert(node3)
tree.Insert(node4)
tree.Insert(node5)
OutputInOrder(tree.GetRootNode())