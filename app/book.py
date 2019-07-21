class Book:
	"""docstring for ClassName"""
	def __init__(self, title,authors,isbn,price):

		price = float(price)
		self.title = title
		self.authors = authors
		self.isbn = isbn
		self.price = price

	def get_title(self):
		return self.title
	
	def get_autthors(self):
		return self.authors

	def get_isbn(self):
		return self.isbn

	def get_price(self):
		return self.price

	def set_title(self, title):
		self.title = title

	def set_authors(self, author):
		self.authors.append(author)

	def set_isbn(self,isbn):
		self.isbn = isbn

	def set_price(self, price):
		self.price = price

	
	def __repr__(self):
		return "< Book %r >" % self.title