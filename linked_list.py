#!/usr/bin/python

class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)

def print_linked_list(node):
	while node:
		print node,
	       	node = node.next 
	print

def print_backward(list):
	print list
	if list == None: 
		print "returning"
		return
	head = list
	tail = list.next
	print "head " + str(head)
	print "tail " + str(tail)
	print_backward(tail)
	print head,
			
if __name__ == "__main__":
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)

	#print node1.cargo, node2.cargo, node3.cargo
	node1.next = node2
	node2.next = node3
	node3.next = node4

	print_linked_list(node1)
	print_backward(node1)	
