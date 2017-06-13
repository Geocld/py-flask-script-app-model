from flask import Flask

# blueprint
from app.api.test.test import test
from app.api.index.index import index

def init_app():
	app = Flask(__name__)

	# regist blueprints
	app.register_blueprint(test)
	app.register_blueprint(index)

	return app