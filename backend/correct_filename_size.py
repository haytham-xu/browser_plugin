
from typing import List
from entity.browser_tab import BrowserTab, Status
from repository.browser_tab_repository import get_all, update_browser_tab
from service.http_service import get_file_name, get_file_size 


def migrate_filename_size():
    all_tabs:List[BrowserTab] = get_all()
    for a_tab in all_tabs:
        has_modify = False
        if a_tab.size == None:
            a_tab.size = get_file_size(a_tab.download_link)
            has_modify = True
        new_filename = get_file_name(a_tab.download_link)
        if a_tab.file_name != new_filename:
            a_tab.file_name = new_filename
            has_modify = True
        if has_modify:
            a_tab.status = Status.TODO.value
            update_browser_tab(a_tab)

if __name__ == '__main__':
    migrate_filename_size()
