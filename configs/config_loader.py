import json
import os

def load_config():

    environment = os.getenv('TEST_ENVIRONMENT', 'production')
    
    config_file_path = f"configs/config.{environment}.json"
    
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
        
    return config