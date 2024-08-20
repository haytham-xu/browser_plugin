
import os
import yaml

config_path = "./config.yaml"

class Config:
    all_config = {}
    def __init__(self):
        self.all_config = yaml.safe_load(open(config_path, 'r')) if os.path.exists(config_path) else {}

    def get_cover_domain(self):
        key = "cover_domain"
        return self.all_config[key] if key in self.all_config else []
    
    def get_db_path(self):
        key = "db_path"
        return self.all_config[key] if key in self.all_config else ""

    def get_overview_uri_path_format(self):
        key = "overview_uri_path_format"
        return self.all_config[key] if key in self.all_config else ""
    
    def get_download_uri_path_format(self):
        key = "download_uri_path_format"
        return self.all_config[key] if key in self.all_config else ""
    
config = Config()
    
