import pygame
import tkinter as tk
from src.getSettings.getSettings import getSettings

root = tk.Tk()
root.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 

print(getSettings().get_screen_settings(screen_width, screen_height))

pygame.init()
program_name = str(getSettings().get_screen_settings(screen_width, screen_height)['program_name'])

width = getSettings().get_screen_settings(screen_width, screen_height)['width']
height = getSettings().get_screen_settings(screen_width, screen_height)['height']

print(width, height)

print(program_name)
print(pygame.display.get_window_size)




def main(runner):
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(program_name)
    while runner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False
                
    
if __name__ == "__main__":
    runner = True          
    main(runner=runner)