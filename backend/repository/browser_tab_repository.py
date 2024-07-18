
import sqlite3
from datetime import datetime
from entity.browser_tab import BrowserTab
from utils.config import config

# status
#   todo -> downloading -> done
#   downloading -> failed
#   failed -> downloading

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
            tab_url TEXT UNIQUE NOT NULL,
            file_name TEXT DEFAULT '',
            size INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def insert_browser_tab(browser_tab: BrowserTab):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO browser_tab (code, created_at, updated_at, status, retry_times, tab_url, file_name, size)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (browser_tab.code, browser_tab.created_at, browser_tab.updated_at, browser_tab.status, 
          browser_tab.retry_times, browser_tab.tab_url, browser_tab.file_name, browser_tab.size))
    conn.commit()
    conn.close()

def get_all_browser_tabs():
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute('SELECT * FROM browser_tab')
    rows = cur.fetchall()
    browser_tabs = []
    for row in rows:
        browser_tab = BrowserTab(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        browser_tabs.append(browser_tab)
    conn.close()
    return browser_tabs

def get_browser_tab_by_id(tab_code):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute('SELECT * FROM browser_tab WHERE code = ?', (tab_code,))
    row = cur.fetchone()
    conn.close()
    if row:
        return BrowserTab(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    return None

def update_browser_tab(browser_tab: BrowserTab):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute('''
        UPDATE browser_tab
        SET code = ?, updated_at = ?, status = ?, retry_times = ?, file_name = ?, size = ?
        WHERE id = ?
    ''', (browser_tab.code, datetime.now(), browser_tab.status, browser_tab.retry_times, 
          browser_tab.file_name, browser_tab.size, browser_tab.id))
    conn.commit()
    conn.close()

def delete_browser_tab(tab_code):
    conn = sqlite3.connect(config.get_db_path())
    cur = conn.cursor()
    cur.execute('DELETE FROM browser_tab WHERE code = ?', (tab_code,))
    conn.commit()
    conn.close()
