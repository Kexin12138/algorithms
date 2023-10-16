from ListNode import NodeList


# method1
def findFirstCommonNodeBySet(head1, head2):
	s = set()
	p, q = head1, head2
	while p:
		s.add(p.data)
		p = p.next

	while q:
		if q.data in s:
			return q
		q = q.next


# method2
def findFirstCommonNodeByStack(head1, head2):
	A, B = [], []
	p, q = head1, head2
	while p:
		A.append(p)
		p = p.next
	while q:
		B.append(q)
		q = q.next

	while A and B:
		a, b = A.pop(), B.pop()
		if a.data != b.data:
			return a.next


if __name__ == '__main__':
	ListA, ListB = NodeList(), NodeList()
	ListA.create_by_list(['a1', 'a2', 'c1', 'c2', 'c3'])
	ListB.create_by_list(['b1', 'b2', 'b3', 'c1', 'c2', 'c3'])
	print('A:', ListA, 'B:', ListB)

	res1 = findFirstCommonNodeBySet(ListA.head, ListB.head)
	res2 = findFirstCommonNodeByStack(ListA.head, ListB.head)
	print(res1, res2)
