import pygame


class Player:
    def __init__(self):
        pass

    def draw_player(self, screen, color, x, y):
        return pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))