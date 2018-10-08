

from device42_app.webapp.app import device_app


device_app.run(debug=True, host='0.0.0.0', threaded=True, port=8000)
