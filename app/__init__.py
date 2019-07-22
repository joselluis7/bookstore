from app import exclusive_book, new_book, used_book
import os


module_names = {'ExclusiveBook':exclusive_book,'NewBook':new_book,'UsedBook':used_book}
csv_path = os.path.join(os.path.abspath(os.path.dirname(__name__)),'basket.csv')
root_path = os.path.abspath(os.path.dirname(__name__))