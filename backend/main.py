

import time
import threading
import datetime

from flask import Flask
from flask_cors import CORS

from controller.browser_tan_controller import app_routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_routes)

def background_task():
    while True:
        now = datetime.datetime.now()
        print(f"执行后台任务: {now}")
        time.sleep(300)

if __name__ == '__main__':
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

    # app.run(debug=True)
    app.run()
