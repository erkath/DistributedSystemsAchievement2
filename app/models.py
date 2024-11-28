from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from app.initial import app

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(app, metadata=MetaData(naming_convention=naming_convention))

# Define models

class ProcessedNumbers(db.Model):
    """
    Все полученные и обработанные валидные числа
    """
    id = db.Column(db.Integer, primary_key=True)
    adding_date = db.Column(db.DateTime)
