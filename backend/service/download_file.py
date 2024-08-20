
import requests

def download_file(download_url, output_path, file_size):
    downloaded_size = 0
    progress = 0
    response = requests.get(download_url, stream=True)
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                downloaded_size += len(chunk)
                if file_size is not None:
                    progress = int((downloaded_size / (file_size*1024*1024) ) * 100)
                file_name = output_path.split("/")[-1]
                print(f"Downloading: {file_name}, size: {file_size}MB, progress: {progress}%")
    return True
