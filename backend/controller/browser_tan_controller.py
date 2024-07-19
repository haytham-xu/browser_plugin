
from flask import request
from flask import Blueprint
from flask import request, jsonify

from utils.config import config
from utils.aid_format import extract_aid
from repository.browser_tab_repository import get_browser_tab_by_code, insert_browser_tab
from entity.browser_tab import BrowserTab
from utils.lock_manager import global_lock

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/tabs', methods=['POST'])
def tabs():
    tabs = request.json['tabs']
    # for each tab,
        # lock DB; search tab by code; if not exist, new and store; or, skip
    for tab in tabs:
        domain_name, path = get_domain_name(tab)
        if domain_name in config.get_cover_domain():
            aid = extract_aid(path)
            with global_lock:
                existing_tab = get_browser_tab_by_code(aid)
                if existing_tab is None:
                    file_name = 'file_name'
                    size = 0
                    new_tab = BrowserTab.new_instance(code=aid, file_name=file_name, size=size)
                    insert_browser_tab(new_tab)
    return jsonify({'message': 'Tabs received and stored.'}), 200

from urllib.parse import urlparse

def get_domain_name(url):
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    path = parsed_url.path
    return domain_name, path
