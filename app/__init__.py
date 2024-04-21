import os
from flask import Flask

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

ADMIN_LOGIN = os.getenv('ADMIN_LOGIN')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

