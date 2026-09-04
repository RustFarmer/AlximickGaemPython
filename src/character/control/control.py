import pygame


class Controls:
    def __init__(self):
        pass

    def move_player(self, pressed, x):
        if pressed[pygame.K_a]:
            x -= 3
            return x
        if pressed[pygame.K_d]:
            x += 3
            return x
        return x
