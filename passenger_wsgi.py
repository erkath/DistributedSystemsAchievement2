import imp
import os
import sys
from app import app


sys.path.insert(0, os.path.dirname(__file__))
application = app
