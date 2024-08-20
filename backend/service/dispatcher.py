
import re
import time
from typing import List

from datetime import datetime
from repository.browser_tab_repository import get_all_need_downloaded, update_browser_tab
from service.download_file import download_file
from entity.browser_tab import Status, BrowserTab

def download_dispatcher():
    browser_tabs:List[BrowserTab] = get_all_need_downloaded()
    for a_tab in browser_tabs:
        a_tab.status = Status.IN_PROGRESS.value
        a_tab.updated_at = datetime.now()
        update_browser_tab(a_tab)
        res = download_file(a_tab.download_link, "./temp/{}.zip".format(sanitize_filename(a_tab.file_name)), a_tab.size)
        if res:
            a_tab.status = Status.COMPLETED.value
            a_tab.updated_at = datetime.now()
            update_browser_tab(a_tab)
        time.sleep(10)
        
def sanitize_filename(filename: str) -> str:
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    sanitized = re.sub(invalid_chars, '_', filename)
    return sanitized
