from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import threading
import requests
import os
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
CORS(app)

class Tab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tab_url = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='TODO')
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    type = db.Column(db.String(20), default='DOWNLOAD')
    file_name = db.Column(db.String(120), default='')
    retry_times = db.Column(db.Integer, default=0)
    size = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

download_progress = {}

@app.route('/tabs', methods=['POST'])
def tabs():
    tabs = request.json['tabs']
    for tab in tabs:
        existing_tab = Tab.query.filter_by(tab_url=tab).first()
        if existing_tab is None:
            new_tab = Tab(tab_url=tab)
            db.session.add(new_tab)
    db.session.commit()
    return jsonify({'message': 'Tabs received and stored.'}), 200

def download_file(tab):
    try:
        tab.status = 'IN_PROGRESS'
        db.session.commit()
        response = requests.get(tab.tab_url, stream=True)
        file_path = os.path.join('download', tab.file_name)
        downloaded_size = 0
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    progress = (downloaded_size / tab.size) * 100
                    download_progress[tab.tab_url] = {
                        'file_name': tab.file_name,
                        'status': tab.status,
                        'size': tab.size,
                        'progress': progress
                    }
                    print(f"download file: {tab.file_name}, size: {tab.size}, progress: {progress}%")
        tab.status = 'DONE'
        db.session.commit()
    except Exception as e:
        tab.status = 'FAILED'
        db.session.commit()
        print(f"Failed to download file: {tab.file_name}, error: {str(e)}")

def check_and_download():
    while True:
        tabs = Tab.query.filter(Tab.status.in_(['TODO', 'FAILED'])).all()
        for tab in tabs:
            if tab.status == 'FAILED':
                tab.retry_times += 1
            threading.Thread(target=download_file, args=(tab,)).start()
        time.sleep(5)

# threading.Thread(target=check_and_download).start()

if __name__ == '__main__':
    app.run(debug=True)
