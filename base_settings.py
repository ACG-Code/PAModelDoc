import os
import sys

APP_NAME = 'ACG Model Documenter'
APP_VERSION = '7.0.0'

if getattr(sys, 'frozen', False):
    APPLICATION_PATH = os.path.dirname(sys.executable)
else:
    APPLICATION_PATH = os.path.dirname(__file__)
