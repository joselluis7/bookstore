
class Basket:
	"""docstring for ClassName"""
	def __init__(self):
		self.books = []
		self.total = 0.0
		self.count = 0

	def set_total(self,total):
		self.total = total

	def set_book(self,book):
		self.books.append(book)
		self.count += 1
		self.total += book.price