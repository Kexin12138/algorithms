class Node:
	def __init__(self, var=None, next=None):
		self.var = var
		self.next = next

def hasCycle(head):
	seen = set()
	while head:
		if head in seen:
			return True
		seen.add(head)
		head = head.next
	return False

def detectcycle(head):
	fast,slow = head,head
	while True:
		if not (fast and fast.next) : return
		fast,slow = fast.next.next,slow.next
		if fast == slow: break
	fast = head
	while fast != slow:
		fast, slow = fast.next, slow.next
	return fast
