from black import main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from db.loginManagerService import login_manager
from db.db import db
from routes.admin import admin
from routes.orders import orders

# from routes.orders import orders
# from routes.orderdetails import orderDetails

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)
Migrate(app, db)

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(orders)
# app.register_blueprint(orderDetails)