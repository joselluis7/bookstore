from app.helpers.utils import currency_format, list_string
from app.basket import Basket
from app import module_names
import csv,sys,os,argparse


parse = argparse.ArgumentParser(description='bookstore application')
parse.add_argument("--file","-f",help="a path of csv file")
parse.add_argument("--displayauthors",help="print prive vs price with discount",action='store_true')
def main():
	args = parse.parse_args()
	#print("Passed file: %s "%args.file)
	csv_path = "path/invalido"
	basket.display_books()

if __name__ == '__main__':
	sys.exit(main())