from app import main as module_main
import sys, argparse


parse = argparse.ArgumentParser(description='bookstore application')
parse.add_argument("--file","-f",help="a path of csv file")
parse.add_argument("--displayauthors",help="print prive vs price with discount",action='store_true')
def main():
	args = parse.parse_args()
	print("Passed file: %s "%args.file)
	module_main.get_booklist()

if __name__ == '__main__':
	sys.exit(main())