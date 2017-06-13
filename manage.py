import os
from flask_script import Manager
from app import init_app

app = init_app()

manager = Manager(app)

if __name__=='__main__':
    manager.run()