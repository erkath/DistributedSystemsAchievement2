from flask import Flask
import logging

from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


def create_app():
    local_app = Flask(__name__)
    local_app.config.from_object(Config)
    return local_app


app = create_app()
