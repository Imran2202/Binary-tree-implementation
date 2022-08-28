class Node:
	def __init__(self, data, parent_node=None):
		self.data = data
		self.left_node = None
		self.right_node = None
		self.parent_node = parent_node


class BST:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)

		else:
			self.insert_node(data, self.root)

	def insert_node(self,data, node):
		if data < node.data:
			if node.left_node:
				self.insert_node(data, node.left_node)
			else:
				node.left_node = Node(data, node)
		else:
			if node.right_node:
				self.insert_node(data, node.right_node)
			else:
				node.right_node = Node(data, node)

	def remove(self, data):
		if self.root:
			self.remove_node(data, self.root)

	def remove_node(self, data, node):
		if not node:
			return 

		if data > node.data:
			self.remove_node(data, node.right_node)
		elif data < node.data:
			self.remove_node(data, node.left_node)
		else:

			#Leaf node
			if node.left_node is None and node.right_node is None:
				print("Removing leaf node:",data)
				parent = node.parent_node

				if parent and parent.right_node == node:
					parent.right_node = None 
				elif parent and parent.left_node == node:
					parent.left_node = None 
				else:
					self.root = None

			# Single left child
			elif node.left_node and node.right_node is None:
				print("Removing single left child node:",data)
				parent = node.parent_node

				if parent and parent.left_node == node:
					parent.left_node = node.left_node
				elif parent and parent.right_node == node:
					parent.right_node = node.left_node
				else:
					self.root = node.left_node

				node.left_node.parent = parent

			# Single right child
			elif node.left_node is None and node.right_node:
				print("Removing single right node:",data)
				parent = node.parent_node

				if parent and parent.left_node == node:
					parent.left_node = node.right_node
				elif parent and parent.right_node == node:
					parent.right_node = node.right_node
				else:
					self.root = node.right_node

				node.right_node.parent = parent

			# Two child
			elif node.left_node and node.right_node:
				print("Removing two child node:",data)
				predecessor = self.predecessor(node.left_node)

				tmp = predecessor.data
				predecessor.data = node.data
				node.data = tmp

				self.remove_node(data, predecessor)



	def predecessor(self, node):
		if node.right_node:
			return self.predecessor(node.right_node)
		return node


	def get_min(self):
		if self.root:
			return self.get_min_value(self.root)

	def get_min_value(self, node):
		if node.left_node:
			return self.get_min_value(node.left_node)

		return node.data

	def get_max(self):
		if self.root:
			return self.get_max_value(self.root)

	def get_max_value(self, node):
		if node.right_node:
			return self.get_max_value(node.right_node)

		return node.data

	# Inorder traversal(Recursive approach)
	def rec_traversal(self):
		def traversal_inorder(node):
			if node.left_node:
				traversal_inorder(node.left_node)
				print(node.data)
				traversal_inorder(node.right_node)
		traversal_inorder(self.root)

	#Inorder traversal(Iterative approach)
	def it_traversal(self):
		def traversal_inorder(node):
			stack = []
			while stack or node:

				while node:
					stack.append(node)
					node = node.left_node
				
				node = stack.pop()
				print(node.data)
				node = node.right_node

		traversal_inorder(self.root)

	# Preorder traversal(Recursive approach)
	def preorder_traversal(self):
		def traversal_preorder(node):
			if node:
				print(node.data)
				traversal_preorder(node.left_node)
				traversal_preorder(node.right_node)
		traversal_preorder(self.root)

	def treeSum(self):
		self.stack = []
		self.count = 0
		def treePathsSum(node):
			if node:
				self.stack.append(node.data)
				treePathsSum(node.left_node)
				if not node.right_node and not node.left_node:
					length = len(self.stack)
					if length > self.count:
						self.count = length
				treePathsSum(node.right_node)
				self.stack.pop()
		treePathsSum(self.root)
		print(self.count)


	def MergeTrees(self,t1, t2):
		if (not t1):
			return t2
		if (not t2):
			return t1
		t1.data += t2.data
		t1.left_node = MergeTrees(t1.left_node, t2.left_node)
		t1.right_node = MergeTrees(t1.right_node, t2.right_node)
		return t1





first = BST()
first.insert(9)
first.insert(16)
first.insert(4)
first.insert(23)
first.insert(12)
first.insert(8)
first.insert(7)
first.insert(18)
first.insert(3)
# first.remove(7)

# first.preorder_traversal()


# print("Max:", first.get_max())

second = BST()
second.insert(1)
second.insert(0)
second.insert(1)
second.insert(1)
second.insert(0)
second.insert(1)
second.insert(0)
second.insert(1)
second.insert(0)
second.insert(1)

second.treeSum()

third = BST()
third.MergeTrees(first.root,second.root)