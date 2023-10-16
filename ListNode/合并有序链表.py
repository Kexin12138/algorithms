from ListNode import NodeList, Node


def mergeTwoNodeList(headA, headB):
	merge = NodeList(head=Node())
	head = merge.head
	p, q = headA, headB

	while p and q:
		if p.data > q.data:
			head.next = q
			q = q.next
		else:
			head.next = p
			p = p.next
		head = head.next
	head.next = p if p else q
	return NodeList(head=merge.head.next)


if __name__ == '__main__':
	ListA, ListB = NodeList(), NodeList()
	ListA.create_by_list([1, 2, 4, 7, 8])
	ListB.create_by_list([1, 3, 5, 6, 10, 11])
	print('A:', ListA, 'B:', ListB)

	print(mergeTwoNodeList(ListA.head, ListB.head))
