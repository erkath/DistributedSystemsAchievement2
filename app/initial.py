from flask import Flask
import logging

from config import Config


def create_app():
    local_app = Flask(__name__)
    local_app.config.from_object(Config)
    return local_app


app = create_app()
