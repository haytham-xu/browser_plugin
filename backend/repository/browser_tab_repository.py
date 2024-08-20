
import sqlite3
from datetime import datetime
from entity.browser_tab import BrowserTab, Status
from utils.config import config

# status
#   todo -> downloading -> done
#   downloading -> failed
#   failed -> downloading

table_name = "browser_tab"

def init_db():
    if not is_table_exists():
        create_table()
    
def is_table_exists():
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    result = cur.fetchone()
    conn.close()
    return result is not None

def create_table():
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS browser_tab (
            id INTEGER PRIMARY KEY,
            code TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'TODO',
            retry_times INTEGER DEFAULT 0,
            file_name TEXT DEFAULT '',
            size INTEGER DEFAULT 0,
            download_link TEXT DEFAULT ''
        )
    ''')
    conn.commit()
    conn.close()

def insert_browser_tab(browser_tab: BrowserTab):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f'''
        INSERT INTO {table_name} (code, created_at, updated_at, status, retry_times, file_name, size, download_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (browser_tab.code, browser_tab.created_at, browser_tab.updated_at, browser_tab.status.value, browser_tab.retry_times, browser_tab.file_name, browser_tab.size, browser_tab.download_link))
    conn.commit()
    conn.close()
    
def get_all():
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM {table_name}''')
    rows = cur.fetchall()
    browser_tabs = []
    for row in rows:
        browser_tab = BrowserTab(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        browser_tabs.append(browser_tab)
    conn.close()
    return browser_tabs

def get_all_need_downloaded():
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM {table_name} WHERE status IN (?, ?)''', (Status.TODO.value, Status.FAILED.value))
    rows = cur.fetchall()
    browser_tabs = []
    for row in rows:
        browser_tab = BrowserTab(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        browser_tabs.append(browser_tab)
    conn.close()
    return browser_tabs

def get_browser_tab_by_code(tab_code):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM {table_name} WHERE code = ?''', (tab_code,))
    row = cur.fetchone()
    conn.close()
    if row:
        return BrowserTab(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    return None

def update_browser_tab(browser_tab: BrowserTab):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f'''
        UPDATE {table_name}
        SET updated_at = ?, status = ?, retry_times = ?, file_name = ?, size = ?
        WHERE id = ?
    ''', (datetime.now(), browser_tab.status, browser_tab.retry_times, browser_tab.file_name, browser_tab.size, browser_tab.id))
    conn.commit()
    conn.close()

def delete_browser_tab(tab_code):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute(f'''DELETE FROM {table_name} WHERE code = ?''', (tab_code,))
    conn.commit()
    conn.close()
