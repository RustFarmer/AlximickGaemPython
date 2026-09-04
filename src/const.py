from dataclasses import dataclass
from pathlib import Path


def get_absolute_path() -> Path:
    return Path(__file__).resolve().parent


file_path = get_absolute_path()
print(file_path)


@dataclass
class FilePath:
    settingsWordData_json_file_Path: str = f"{file_path}\\word\\settingsWordData\\settingsWordData.json"
    settingsScreenData_json_file_path: str = f'{file_path.parent}\\screenData\\settingsScreen.json'


@dataclass
class JsonKey:
    program_name = "title"
    size_program_width = "width"
    size_program_height = "height"
