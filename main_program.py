#-*-encoding:utf-8-*- 
from app.helpers.utils import list_string
from app.basket import Basket
from app import module_names, csv_path
import csv,sys,os



def main():
	basket = Basket()
	with open(csv_path) as csv_file:
		csv_data = csv.DictReader(csv_file)	
		for row in csv_data:
			Book = getattr(module_names[row['type']], row['type'])
			book = Book(row['title'],row['authors'].split('|'), row['isbn'],row['price'])
			basket.set_book(book)

	for book in basket.books:
		authors = list_string(book.authors)
		print("€ %6.2f " %(book.price) + "[{0}] {1}: {2} - {3}".format(book.TYPE,book.isbn,book.title,authors))
	print("€ %6.2f - Total"%basket.total)

if __name__ == '__main__':
	sys.exit(main())
	
		

