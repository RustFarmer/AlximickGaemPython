import pygame
from src.character.Skill.DrawUsedSkill.DrawSkillUsed import draw_skill


class UseSkill:
    def __init__(self):
        pass

    def mouse_use(self, mouse_pressed, screen: pygame.display, skill_image: pygame.image, x):
        if mouse_pressed[0]:
            draw_skill(screen, skill_image, x)
