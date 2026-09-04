import json
from src.const import FilePath, JsonKey


class getSettings:
    def __init__(self):
        self.size_screen_height = None
        self.size_screen_width = None
        self.settings_word_data_json_file_path = FilePath().settingsWordData_json_file_Path
        self.settings_screen_data_json_file_path = FilePath().settingsScreenData_json_file_path

        self.settings_data = None
        self.program_name = None

    def __load_settings_word__(self) -> dict:
        try:
            with open(self.settings_word_data_json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except EnvironmentError as e:
            return e

    def __load_settings_screen__(self) -> dict:
        try:
            with open(self.settings_screen_data_json_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except EnvironmentError as e:
            return e

    def get_screen_settings(self, width_screen, height_screen):
        width = width_screen
        height = height_screen
        self.settings_data: dict = self.__load_settings_screen__()

        print(self.settings_data)

        self.program_name = self.settings_data.get(JsonKey.program_name, '')

        program_dict = {"program_name": self.program_name}

        self.size_screen_width = self.settings_data[JsonKey.size_program_width]
        self.size_screen_height = self.settings_data[JsonKey.size_program_height]

        if [self.size_screen_width, self.size_screen_height] != ["default", "default"]:
            if self.size_screen_width == "default":
                program_dict["width"] = width
                print(program_dict, "lk3h4p6o=-------------------------g832yu0")

            if self.size_screen_width == "default":
                program_dict["height"] = height

            print(program_dict, "lk3h4p6og832yu0")
            return program_dict

        return {
            "program_name": self.program_name,
            "width": self.settings_data.get(JsonKey.size_program_width, width),
            "height": self.settings_data.get(JsonKey.size_program_height, height)
        }
