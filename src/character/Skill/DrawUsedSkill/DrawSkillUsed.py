import pygame


def draw_skill(screen: pygame.display, skill_image: pygame.image, x, y=500):
    return screen.blit(skill_image, (x, y))
