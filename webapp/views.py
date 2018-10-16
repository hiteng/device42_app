

from device42_app.webapp.app import device_app
from flask import render_template

@device_app.route("/", methods=["GET"])
def home():

    return render_template("inventory.html")
