from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate


from Web_app import Web_app


My_db = SQLAlchemy(Web_app)

migrate =  Migrate(Web_app,My_db)
