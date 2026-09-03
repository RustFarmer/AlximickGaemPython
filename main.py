import pygame
from src.getSettings.getSettings import getSettings

print(getSettings().__load_settings_word__())

pygame.init()



def main(runner):
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    while runner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False
                
    
if __name__ == "__main__":
    runner = True
                
    main(runner=runner)