from ListNode import NodeList


def findMidNode(head):
	slow, fast = head, head
	while fast:
		if not fast.next:
			return slow
		fast = fast.next.next
		slow = slow.next
	return slow


def findReverseK(head, k):
	p, q = head, head
	for _ in range(k):
		q = q.next
	while q:
		q = q.next
		p = p.next
	return p


def rotateNodeList(head, k):
	p, q = head, head
	for _ in range(k):
		q = q.next
	while q.next:
		q = q.next
		p = p.next
	# 此时q为尾节点，p为新链表尾节点
	q.next = head
	new_head = p.next
	p.next = None
	return new_head


if __name__ == '__main__':
	ListA, ListB = NodeList(), NodeList()
	ListA.create_by_list([1, 2, 4, 7, 8])
	ListB.create_by_list([1, 3, 5, 6, 10, 11])
	print('A:', ListA, 'B:', ListB)

	print(findMidNode(ListA.head))
	print(findMidNode(ListB.head))
	print(findReverseK(ListA.head, 2))
	print(NodeList(head=rotateNodeList(ListA.head, 2)))
