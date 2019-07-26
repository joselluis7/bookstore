from flask import jsonify
from api import app
from pathlib import Path
import sys, os, csv

#GET PROJECT DIR
basedir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__name__))))
app_path = os.path.join(basedir,"app")
csv_path = os.path.join(basedir,"basket.csv")
sys.path.insert(1, app_path)  
sys.path.insert(2, basedir) 

from basket import Basket
from app import module_names


@app.route("/add", methods=["GET"])
def add():
	return "metódo to add"

@app.route("/bookstoreapi", methods=["GET"])
def get():
	return "metódo to get"

