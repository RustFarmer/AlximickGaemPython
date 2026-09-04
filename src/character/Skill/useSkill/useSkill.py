import pygame
from src.character.Skill.MovedSkill import moved_skill
from src.character.Skill.DrawUsedSkill.DrawSkillUsed import draw_skill


class UseSkill:
    def __init__(self, player_y):
        self.skill_active = False
        self.skill_x = None
        self.skill_speed = 10

        self.skill_cooldown = 500
        self.last_skill_use_time = 0

        self.fer_bol = pygame.image.load("src/character/Skill/DrawUsedSkill/skillImageUsed/img.png")
        self.skill_y = player_y + 30 - self.fer_bol.get_height() // 2

    def update(self, screen, mouse_pressed, mouse_pos, obj_blit, player_x, screen_width):
        current_time = pygame.time.get_ticks()

        if mouse_pressed[0] and obj_blit.collidepoint(mouse_pos) and not self.skill_active and (
                current_time - self.last_skill_use_time >= self.skill_cooldown):
            self.skill_active = True
            self.skill_x = player_x
            self.last_skill_use_time = current_time

        if self.skill_active:
            self.skill_x = moved_skill(self.skill_x, self.skill_speed)

            if self.skill_x > screen_width:
                self.skill_active = False

            draw_skill(screen, self.fer_bol, self.skill_x, self.skill_y)

        return self.skill_active
