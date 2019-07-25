#-*-encoding:utf-8 -*-
from app.helpers.utils import list_string
from app.basket import Basket
from app import module_names, csv_path
import csv,sys,os,argparse


parse = argparse.ArgumentParser(description='bookstore application')
#parse.add_argument("--file","-f",help="a path of csv file")
parse.add_argument("--displayauthors","-d",help="print price vs price with discount",action='store_true')
def main():
	args = parse.parse_args()
	basket = Basket()

	if args.displayauthors:
		with open(csv_path) as csv_file:
			csv_data = csv.DictReader(csv_file)	
			for row in csv_data:
				Book = getattr(module_names[row['type']], row['type'])
				book = Book(row['title'],row['authors'].split('|'), row['isbn'],row['price'])
				basket.set_book(book)
	
		for book in basket.books:
			authors = list_string(book.authors)
			price = book.price + book.price*book.DISCOUNT
			print("€ %5.2f/%5.2f: " %(price,book.price) + " {0} - {1}".format(book.title,authors))
		print("€ %6.2f - Total"%basket.total)
	else:
		print("Use o parametro -d ou --help")
if __name__ == '__main__':
	sys.exit(main())