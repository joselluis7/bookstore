from app.book import Book

class NewBook(Book):
	"""docstring for LivroNovo"""
	DISCOUNT = 0.1
	def __init__(self,title,authors,isbn,price):
		Book.__init__(self,title,authors,isbn,price)
		self.set_price(self.price)
		self.TYPE = "Novo"
	
	def set_price(self,price):
		self.price = self.price - price*self.DISCOUNT