
class BrowserTab:
    def __init__(self, id, code, created_at, updated_at, status, retry_times, tab_url, file_name, size):
        self.id = id
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at
    
        self.status = status
        self.retry_times = retry_times
    
        self.tab_url = tab_url
        self.file_name = file_name
        self.size = size
        
    def new_instance(self, code, tab_url, file_name, size):
        pass
    
        