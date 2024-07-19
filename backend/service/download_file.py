
import os
import time
import requests

download_progress = {}

# def download_file(tab):
#     try:
#         tab.status = 'IN_PROGRESS'
#         db.session.commit()
#         response = requests.get(tab.tab_url, stream=True)
#         file_path = os.path.join('download', tab.file_name)
#         downloaded_size = 0
#         with open(file_path, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     f.write(chunk)
#                     downloaded_size += len(chunk)
#                     progress = (downloaded_size / tab.size) * 100
#                     download_progress[tab.tab_url] = {
#                         'file_name': tab.file_name,
#                         'status': tab.status,
#                         'size': tab.size,
#                         'progress': progress
#                     }
#                     print(f"download file: {tab.file_name}, size: {tab.size}, progress: {progress}%")
#         tab.status = 'DONE'
#         db.session.commit()
#     except Exception as e:
#         tab.status = 'FAILED'
#         db.session.commit()
#         print(f"Failed to download file: {tab.file_name}, error: {str(e)}")

# def check_and_download():
#     while True:
#         tabs = Tab.query.filter(Tab.status.in_(['TODO', 'FAILED'])).all()
#         for tab in tabs:
#             if tab.status == 'FAILED':
#                 tab.retry_times += 1
#             threading.Thread(target=download_file, args=(tab,)).start()
#         time.sleep(5)


# threading.Thread(target=check_and_download).start()
