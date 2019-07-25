from flask import Flask





def create_app():

	app = Flask('bookstore')
	app.config.from_object('app.setting')
	return app