
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# import threading

# import os
# import time

from flask import Flask
from flask_cors import CORS

from controller.browser_tan_controller import app_routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True)
