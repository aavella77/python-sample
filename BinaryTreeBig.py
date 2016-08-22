#!/usr/bin/python

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
	def insertRightChild(self,value):
		self.right = value
	def insertLeftChild(self,value):
		self.left = value
	def printPreOrder(self):
		print self.getNodeValue()
		print self.getLeftChild()
		print self.getRightChild()
	def printInOrder(self):
		print self.getLeftChild()
		print self.getNodeValue()
		print self.getRightChild()
	def printPostOrder(self):
		print self.getLeftChild()
		print self.getRightChild()
		print self.getNodeValue()
 
if __name__ == "__main__":
	binaryTree = BinaryTree(7)
	binaryTree.insertLeftChild(8)
	binaryTree.insertRightChild(9)

	print "    7 "
	print "  8   9"
	print " 1 2 3 4"
	print "* Pre-order"
	binaryTree.printPreOrder()

	print "* In-order"
	binaryTree.printInOrder()

	print "* Post-order"
	binaryTree.printPostOrder()
