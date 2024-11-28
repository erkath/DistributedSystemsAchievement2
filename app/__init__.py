import logging

from flask_babel import Babel
from flask_migrate import Migrate

from app.initial import app
from app.models import db
from app import routes

migrate = Migrate(app, db)


def get_locale():
    return 'ru'


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

logger = logging.getLogger()
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)



