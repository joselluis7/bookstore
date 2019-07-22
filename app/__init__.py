from app import exclusive_book, new_book, used_book
import os,csv
from app.basket import Basket
from app.helpers import utils

module_names = {'ExclusiveBook':exclusive_book,'NewBook':new_book,'UsedBook':used_book}
csv_path = os.path.join(os.path.abspath(os.path.dirname(__name__)),'basket.csv')

#root_path = os.path.abspath(os.path.dirname(__name__))

def get_basket():
	print(csv_path)
	basket = Basket()
	with open(csv_path) as csv_file:
		csv_data = csv.DictReader(csv_file)	
		for row in csv_data:
			Book = getattr(module_names[row['type']], row['type'])
			book = Book(row['title'],row['authors'].split('|'), row['isbn'],row['price'])
			basket.set_book(book)

	return basket

basket = get_basket()