import pygame
import tkinter as tk
from src.getSettings.getSettings import getSettings
from src.word.word import word

root = tk.Tk()
root.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


pygame.init()
program_name = str(getSettings().get_screen_settings(screen_width, screen_height)['program_name'])

width = getSettings().get_screen_settings(screen_width, screen_height)['width']
height = getSettings().get_screen_settings(screen_width, screen_height)['height']


def main(runner):
    word(program_name, runner)


if __name__ == "__main__":
    runner = True
    main(runner=runner)
