from dataclasses import dataclass
from pathlib import Path


def get_absolute_path() -> Path:
    return Path(__file__).resolve().parent


file_path = get_absolute_path()


@dataclass
class FilePath:
    settingsWordData_json_file_Path: str = f"{file_path}/AllDataFIle/settingsWordData/settingsWordData.json"
    settingsScreenData_json_file_path: str = f'{file_path}/AllDataFIle/screenData/settingsScreen.json'


@dataclass
class ImagePath:
    magicPocox: str = f"{file_path.parent}/static/image/skillImageIcon/magicPocox.png"
    enemyImage: str = f"{file_path.parent}/static/image/enemyImage/defaultEnemy.png"
    backgroundImage: str = f"{file_path.parent}/static/image/background/af.png"
    skillImageFireball: str = f"{file_path.parent}/static/image/skillImageUsed/img.png"


@dataclass
class JsonKey:
    program_name = "title"
    size_program_width = "width"
    size_program_height = "height"
