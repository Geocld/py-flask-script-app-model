from flask import Flask

# blueprint
from app.api.test.test import test
from app.api.index.index import index

def init_app(dev=False):
	app = Flask(__name__)

	# Load the default configuration
	app.config.from_pyfile('../settings/default.py')

	if dev:
		app.config.from_pyfile('../settings/development.py')
	else:
		app.config.from_pyfile('../settings/production.py')

	# print(app.config['SECRET_KEY'])
	print(app.config['TYPE'])

	# regist blueprints
	app.register_blueprint(test)
	app.register_blueprint(index)

	return app