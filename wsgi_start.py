import logging

from app import app
from waitress import serve
from paste.translogger import TransLogger

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

serve(TransLogger(app, setup_console_handler=True, logging_level=logging.INFO),  port=5000)
