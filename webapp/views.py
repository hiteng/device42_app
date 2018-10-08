

from device42_app.webapp.app import device_app

device_app.route("/", methods=["GET"])
def home():

    return "Welcome to device42"
