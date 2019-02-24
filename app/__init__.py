from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# flask_migrate allows for model to db migrations with up and down like Ruby on Rails
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Set login view for authorization
login.login_view = 'login'

from app import routes, models
