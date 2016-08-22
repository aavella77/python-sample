#!/usr/bin/python

# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())
            
# test tree

def testTree():
    myTree = BinaryTree("grandmother")
    myTree.insertRight("daughter")
    myTree.insertLeft("son")
    myTree.insertLeft("gd1")
    printTree(myTree)
    exit(1)
    myTree.insertRight("gs1")
    myTree.insertRight("grandson")
    printTree(myTree)
    exit(1)
    #myTree.insertRight("grandson")
    #myTree.insertLeft("granddaugther")
    printTree(myTree)

if __name__ == "__main__":
    testTree()
