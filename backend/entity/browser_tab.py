
import datetime

class BrowserTab:

    def __init__(self, id, code, created_at, updated_at, status, retry_times, file_name, size):
        self.id = id
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at
    
        self.status = status
        self.retry_times = retry_times
    
        self.file_name = file_name
        self.size = size
    
    @classmethod
    def new_instance(cls, code, file_name, size):
        return cls(None, code, datetime.now(), datetime.now(), 'TODO', 0, file_name, size)
    
        