


import os

from flask import Flask

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "templates")
device_app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='static/templates')


from device42_app.webapp import views



"""
print os.path.abspath(__file__)
print __file__
print os.path.dirname(os.path.abspath(__file__))
print os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "templates")

/Users/hitendra/workspace/device42_app/webapp/app.py
/Users/hitendra/workspace/device42_app/webapp/app.py
/Users/hitendra/workspace/device42_app/webapp
/Users/hitendra/workspace/device42_app/webapp/static/templates
"""
