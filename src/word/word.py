import pygame
from src.character.RedyPlayer import Player
from src.character.Skill.drawSkillIcon.drawSkillIcon import DrawSkillButton
from src.character.control.control import Controls
from src.character.Skill.DrawUsedSkill.DrawSkillUsed import draw_skill
from src.character.Skill.MovedSkill import moved_skill


def word(program_name, runner):
    x = 100
    y = 500
    skill_x = None
    skill_active = False
    skill_speed = 10

    fer_bol = pygame.image.load("src/character/Skill/DrawUsedSkill/skillImageUsed/img.png")
    skill_y = y + 30 - fer_bol.get_height() // 2

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(program_name)
    background_image = pygame.image.load('static/image/af.png')

    screen_width = screen.get_width()

    while runner:
        pressed = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False

        x = int(Controls().move_player(pressed, x))
        print(x)
        screen.blit(background_image, (-1, -1))
        screen.blit(DrawSkillButton().draw_button_skill(), (1800, 900))
        Player().draw_player(screen, (255, 100, 34), x, y)

        if mouse_pressed[0] and not skill_active:
            skill_active = True
            skill_x = x

        if skill_active:
            skill_x = moved_skill(skill_x, skill_speed)
            if skill_x > screen_width:
                skill_active = False
            draw_skill(screen, fer_bol, skill_x, skill_y)

        pygame.display.flip()