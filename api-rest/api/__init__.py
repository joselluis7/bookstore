from flask import Flask





app = Flask('bookstore')
app.config.from_object('api.setting')

from api.controllers import views