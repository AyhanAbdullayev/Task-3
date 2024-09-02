from flask import Flask

Web_app = Flask(__name__)

Web_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost:3306/Flask"
Web_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from Controller import *
from Extensions import *
from Models import *


if __name__ == "__main__":
    Web_app.run(debug = True)