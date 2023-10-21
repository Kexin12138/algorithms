class Node:
	def __init__(self, var=None, last = None, next=None):
		self.var = var
		self.next = next
		self.last = last

class JosephRing:
	def __init__(self,n,k,m):
		self.n = n # 人数
		self.k = k # 起点
		self.m = m # 间距

		self.ring = self.create()

	def create(self):
		group = [Node(i) for i in range(1,self.n+1)]
		for i in range(self.n):
			group[i].last = group[(i-1)%self.n]
			group[i].next = group[(i+1)%self.n]
		return group[self.k-1]

	def display(self):
		head, cur = self.ring,self.ring
		while True:
			print(cur.var, end='->')
			cur = cur.next
			if cur.var == head.var:
				break
		print()

	def run(self):
		cur = self.ring
		for times in range(self.n-1):
			for _ in range(self.m-1):
				cur = cur.next
			if cur.var == self.ring.var:
				self.ring = cur.next
			cur.last.next = cur.next
			cur.next.last = cur.last
			cur = cur.next
			# self.display()
		print('result:',self.ring.var)

	def inverse_run(self):
		cur = self.ring
		for times in range(self.n-1):
			for _ in range(self.m-1):
				cur = cur.last
			if cur.var == self.ring.var:
				self.ring = cur.last
			cur.last.next = cur.next
			cur.next.last = cur.last
			self.display()

if __name__ == '__main__':
	n = 5
	for i in range(1,n+1):
		ring = JosephRing(i,k=1,m=2)
		ring.run()
	# ring.inverse_run()
	# ring = JosephRing(5,k=1,m=2)
	# ring.inverse_run()