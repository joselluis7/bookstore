from app.book import Book

class UsedBook(Book):
	"""docstring for ClassName"""
	DISCOUNT = 0.25
	def __init__(self,title,authors,isbn,price):
		Book.__init__(self,title,authors,isbn,price)
		self.set_price(self.price)
		self.TYPE = "Usado"

	def set_price(self,price):
		self.price = self.price - price*self.DISCOUNT

	def get_realprice(self):
		return self.price + price*self.DISCOUNT