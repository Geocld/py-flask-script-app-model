import os
from flask_script import Manager
from app import init_app

app = init_app()

# if os.path.exists('.env'):
#     print('Importing environment from .env...')
#     for line in open('.env'):
#         var = line.strip().split('=')
#         if len(var) == 2:
#             os.environ[var[0]] = var[1]

manager = Manager(app)

if __name__=='__main__':
    manager.run()