
from datetime import datetime
from enum import Enum

class Status(Enum):
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
    
class BrowserTab:

    def __init__(self, id, code, created_at, updated_at, status: Status, retry_times, file_name, size, download_link):
        self.id = id
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at
    
        self.status = status
        self.retry_times = retry_times
    
        self.file_name = file_name
        self.size = size
        self.download_link = download_link
    
    @classmethod
    def new_instance(cls, code, file_name, size, download_link):
        return cls(None, code, datetime.now(), datetime.now(), Status.TODO, 0, file_name, size, download_link)
    
        