
import re
import requests
import html
import time
from urllib.parse import urlparse, parse_qs, unquote

def get_file_meta(download_tab_url):
    html_content  = get_html_content(download_tab_url)
    download_link = extract_download_link(html_content)
    file_size_mb = get_file_size(download_link)
    file_name = get_file_name(download_link)
    return download_link, file_name, file_size_mb

def get_file_size(url):
    response = request_with_retries(url)
    if response == None or response.headers.get('Content-Length') == None:
        print("Error: Failed to get file size.")
        return None
    file_size = response.headers.get('Content-Length')
    file_size_mb = int(file_size) / (1024 * 1024)
    return int(file_size_mb)



def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed in request: {e}")
        return None

def extract_download_link(html):
    pattern = r'href="(//v1\.wzip\.download/down/\d+/[a-f0-9]+\.zip\?n=[^"]+)"'
    match = re.search(pattern, html)
    if match:
        return f"https:{match.group(1)}"
    return None

def get_file_name(download_link):
    
    match = re.search(r'\?.*?=(.*)', download_link)
    param_value = match.group(1) 
    final_value = html.unescape(param_value)
    return final_value     


def request_with_retries(url, max_retries=3, retry_delay=2):
    for attempt in range(max_retries):
        try:
            response = requests.head(url, allow_redirects=True)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Request failed.")
                return None
               
    
if __name__ == '__main__':
    pass
