from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:enki@localhost/magnet?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = '928bb454f90046e5bab34471105bac54'
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

app.debug = True
api = Api(app)

from app.home import home as home_blueprint

app.register_blueprint(home_blueprint)