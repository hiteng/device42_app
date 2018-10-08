

from flask import Flask


device_app = Flask(__name__)

from device42_app.webapp import views