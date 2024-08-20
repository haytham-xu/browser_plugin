
import re
from urllib.parse import urlparse
from utils.config import config

def get_domain_name(url):
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    path = parsed_url.path
    return domain_name, path

def extract_aid(url):
    pattern = config.get_overview_uri_path_format().replace("{aid}", r"(\d+)")
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_download_path(aid):
    return config.get_download_uri_path_format().replace("{aid}", str(aid))

def is_match(uri_path):
    pattern = config.get_overview_uri_path_format().replace("{aid}", r"(\d+)")
    if re.fullmatch(pattern, uri_path):
        return True
    return False
