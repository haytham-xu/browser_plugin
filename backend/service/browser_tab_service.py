
from utils.config import config
from utils.aid_format import extract_aid, is_match, get_domain_name, get_download_path
from repository.browser_tab_repository import get_browser_tab_by_code, insert_browser_tab
from entity.browser_tab import BrowserTab

from service.http_service import get_file_meta

# for each tab,
    # lock DB; search tab by code; if not exist, new and store; or, skip
def store_tab(tab_url):
    domain_name, path = get_domain_name(tab_url)
    if domain_name in config.get_cover_domain() and is_match(path):
        aid = extract_aid(path)
        existing_tab = get_browser_tab_by_code(aid)
        if existing_tab is None:
            download_link, file_name, file_size_mb = get_file_meta("https://{}{}".format(domain_name, get_download_path(aid)))
            new_tab = BrowserTab.new_instance(code=aid, file_name=file_name, size=file_size_mb, download_link=download_link)
            insert_browser_tab(new_tab)
