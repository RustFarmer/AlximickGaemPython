import json
from src.const import FilePath


class getSettings:
    def __init__(self):
        self.settings_word_data_json_file_path = FilePath().settingsWordData_json_file_Path
        self.settings_screen_data_json_file_path = FilePath().settingsScreenData_json_file_path
    
    def __load_settings_word__(self) -> dict:
        try:
            with open(self.settings_word_data_json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except EnvironmentError as e:
            return e
    
    def __load_settings_screen__(self) -> dict:
        try:
            with open() as f:
                ...
        except EnvironmentError as e:
            return e
    
    def get_screen_settings():
        pass