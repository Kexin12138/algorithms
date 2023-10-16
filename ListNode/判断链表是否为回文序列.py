from ListNode import NodeList


def isPalindrome(head):
	ls = []
	p = head
	while p:
		ls.append(p)
		p = p.next
	p = head
	while p:
		cur = ls.pop()
		if cur.data != p.data:
			return False
		p = p.next
	return True


# 使用快慢指针
def isPalindrome_(head):
	slow, fast = head, head
	# 栈和队列分别存储前后半链表
	A, B = [], []
	while fast:
		# 单数结点链表尾部，则跳过中间元素
		if not fast.next:
			slow = slow.next
			break
		A.append(slow)
		fast = fast.next.next
		slow = slow.next

	while slow:
		B.append(slow)
		slow = slow.next

	while A and B:
		if A.pop().data != B.pop(0).data:
			return False
	return True


if __name__ == '__main__':
	ListA = NodeList()
	ListA.create_by_list(['a1', 'a2', 'a1', 'a4', 'a1', 'a2', 'a1'])
	ListB = NodeList()
	ListB.create_by_list(['a1', 'a2', 'a4', 'a1', 'a2', 'a1'])

	print(isPalindrome(ListA.head))
	print(isPalindrome(ListB.head))
	print(isPalindrome_(ListA.head))
	print(isPalindrome_(ListB.head))
