
from flask import request
from flask import Blueprint
from flask import request, jsonify

from service.browser_tab_service import store_tab
from utils.lock_manager import global_lock

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/tabs', methods=['POST'])
def tabs():
    with global_lock:
        tabs = request.json['tabs']
        for tab_url in tabs:
            store_tab(tab_url)
        return jsonify({'message': 'Tabs received and stored.'}), 200
