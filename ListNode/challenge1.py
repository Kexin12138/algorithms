class Student:
	def __init__(self, name, language, next=None):
		self.name = name
		self.language = language
		self.next = next

class Camp:
	def init_from_dict(self,dict):
		self.group = [Student(name=name,language=lang) for name, lang in dict]
		for i in range(len(self.group)-1):
			self.group[i].next = self.group[i+1]
		self.nodelist = self.group[0]

	def __str__(self):
		# return '\n'.join([i.name+'\t'+i.language for i in self.group])
		desp = ''
		head = self.nodelist
		while head:
			desp += head.name + '\t' + head.language +'\n'
			head = head.next
		return desp

	def add(self, name, lang):
		cur = self.nodelist
		while cur:
			if cur.language ==lang and (cur.next.language != lang or not cur.next):
				cur.next = Student(name=name, language=lang, next=cur.next)
				break
			cur = cur.next

if __name__ == '__main__':
	dict = [["aa" , "Java"],["ab" , "Java"],["ac" , "Java"],
			["ba" , "CPP"],["bb" , "CPP"],["bc" , "CPP"],
			["ca" , "Python"],["cb" , "Python"] ,["cc " , "Python"]]
	camp = Camp()
	camp.init_from_dict(dict)
	camp.add('jack','CPP')
	print(camp)