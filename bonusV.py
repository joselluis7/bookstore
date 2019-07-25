#-*-encoding:utf-8 -*-
from app.helpers.utils import list_string
from app.basket import Basket
from app import module_names, csv_path
import csv,sys



def main():
	counts = {}
	prices = {}
	basket = Basket()
	with open(csv_path) as csv_file:
		csv_data = csv.DictReader(csv_file)	
		for row in csv_data:
			Book = getattr(module_names[row['type']], row['type'])
			book = Book(row['title'],row['authors'].split('|'), row['isbn'],row['price'])
			if not (row['isbn'] in list(counts)): # not include repeated
				basket.set_book(book)
			count = counts.get(row['isbn'],0) + 1
			counts[row['isbn']] = count
			price = float(prices.get(row['isbn'], 0)) + float(book.price)
			prices[row['isbn']] = price
	for book in basket.books:
		authors = list_string(book.authors)
		print("€ %6.2f "%(prices[book.isbn]) + "({0}) {1}: {2} - {3}".format(counts[book.isbn],book.isbn,book.title,authors))

if __name__ == '__main__':
	sys.exit(main())