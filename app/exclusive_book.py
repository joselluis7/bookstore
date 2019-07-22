from app.book import Book

class ExclusiveBook(Book):
	"""docstring for ClassName"""
	def __init__(self,title,authors,isbn,price):
		Book.__init__(self,title,authors,isbn,price)
		self.TYPE = "Exclusivo"