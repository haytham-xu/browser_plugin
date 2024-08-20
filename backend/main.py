

import time
import threading

from flask import Flask
from flask_cors import CORS

from controller.browser_tan_controller import app_routes
from repository.browser_tab_repository import init_db
from service.dispatcher import download_dispatcher

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_routes)

def background_task():
    while True:
        download_dispatcher()
        time.sleep(60)

if __name__ == '__main__':
    init_db()
    
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

    app.run()
