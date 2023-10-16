from ListNode import NodeList


def del_elem(head, var):
	p = head
	while p.data == var:
		p = p.next
	new_head = p
	while p.next:
		if p.next.data == var:
			p.next = p.next.next
		else:
			p = p.next

	return new_head


if __name__ == '__main__':
	ListA = NodeList()
	ListA.create_by_list(['a1', 'a1', 'a1', 'a4', 'a1', 'a1', 'a1'])
	print('A:', ListA)
	print(del_elem(ListA.head, 'a1'))
