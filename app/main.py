
from app.basket import Basket
from app import module_names, csv_path
from app.helpers import utils

import csv,os


def get_booklist():
	basket = Basket()
	with open(csv_path) as csv_file:
		csv_data = csv.DictReader(csv_file)	
		for row in csv_data:
			Book = getattr(module_names[row['type']], row['type'])
			book = Book(row['title'],row['authors'].split('|'), row['isbn'],row['price'])
			basket.set_book(book)
	for book in basket.books:
		#print(utils.output_format(book.price,book.TYPE,book.isbn,book.title,book.authors))
		pass
