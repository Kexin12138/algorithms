class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		desp = str(self.data) + '->'
		cur = self.next
		while cur:
			desp += str(cur.data) + '->'
			cur = cur.next
		desp += 'end'
		return desp


class NodeList:
	def __init__(self, head=None):
		self.head = head

	def create_by_list(self, ls):
		if not ls:
			return
		else:
			self.head = Node(ls[0])
			cur = self.head
			for items in ls[1:]:
				cur.next = Node(items)
				cur = cur.next

	# add node at tail
	def add(self, node):
		cur = self.head
		while cur:
			cur = cur.next
		cur.next = node
		node.next = None

	def delete(self):
		pass

	def query(self, key):
		cur = self.head
		while cur.next:
			if key == cur.next.data:
				return cur.next

	def __str__(self):
		desp = ''
		cur = self.head
		while cur:
			desp += str(cur.data) + '->'
			cur = cur.next
		desp += 'end'
		return desp

	def isEmpty(self):
		return not self.head.next

	def __len__(self):
		count = 0
		cur = self.head
		while cur.next:
			count += 1
			cur = cur.next
		return count


if __name__ == '__main__':
	nList = NodeList()
	nList.create_by_list([3, 4, 5, 1, 2])
	print(nList)
