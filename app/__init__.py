from app import exclusive_book, new_book, used_book
import os,csv
from app.basket import Basket
from app.helpers import utils

module_names = {'ExclusiveBook':exclusive_book,'NewBook':new_book,'UsedBook':used_book}
csv_path = os.path.join(os.path.abspath(os.path.dirname(__name__)),'basket.csv')