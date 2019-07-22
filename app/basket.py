#-*- encoding:utf-8 -*-
from app.helpers.utils import currency_format, list_string

class Basket:
	"""docstring for ClassName"""
	def __init__(self):
		self.books = []
		self.total = 0.0
		self.count = 0

	def set_total(self,price):
		self.total += price

	def set_book(self,book):
		self.books.append(book)
		self.count += 1
		self.set_total(book.price) 

	def display_books(self):
		#
		for book in self.books:
			price = currency_format(book.price)
			authors = list_string(book.authors)
			print("€ [{1}] {2}: {3} - {4}".format(book.price,book.TYPE,book.isbn,book.title,authors))

		#return "€  ".format(price,class_type,isbn,title,authors)