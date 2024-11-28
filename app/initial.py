from flask import Flask
import logging

from config import Config


def create_app():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[{asctime}] [{levelname}] {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{"
    )

    local_app = Flask(__name__)
    local_app.config.from_object(Config)
    return local_app


app = create_app()
