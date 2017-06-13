from flask import Flask, Blueprint

index = Blueprint('/', __name__, static_folder='static')

@index.route('/')
def root():
	return index.send_static_file('index.html')