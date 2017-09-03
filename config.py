import os

basedir = os.path.realpath(os.path.abspath(os.path.dirname(__file__)))
db_name = 'sqlite:///' + os.path.join(basedir, 'dataBase.db')

SECRET_KEY = 'ourSecret_Key'
