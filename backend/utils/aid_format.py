
import re
from utils.config import config

def extract_aid(url):
    pattern = config.get_overview_uri_path_format().replace("{aid}", r"(\d+)")
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def generate_url(aid):
    return config.get_overview_uri_path_format().replace("{aid}", str(aid))
