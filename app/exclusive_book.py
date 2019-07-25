from app.book import Book

class ExclusiveBook(Book):
	"""docstring for ClassName"""
	DISCOUNT = 0.0
	def __init__(self,title,authors,isbn,price):
		Book.__init__(self,title,authors,isbn,price)
		self.TYPE = "Exclusivo"