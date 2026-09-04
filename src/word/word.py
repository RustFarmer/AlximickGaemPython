import pygame
from src.character.RedyPlayer import Player
from src.character.Skill.drawSkillIcon.drawSkillIcon import DrawSkillButton
from src.character.control.control import Controls
from src.character.Skill.useSkill.useSkill import UseSkill
from src.const import ImagePath


def word(program_name, runner):
    x = 100
    y = 500

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(program_name)
    background_image = pygame.image.load(ImagePath.backgroundImage)

    screen_width = screen.get_width()

    skill = UseSkill(y)

    while runner:
        pressed = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False

        x = int(Controls().move_player(pressed, x))
        screen.blit(background_image, (-1, -1))
        obj_blit = screen.blit(DrawSkillButton().draw_button_skill(), (1800, 900))
        Player().draw_player(screen, (255, 100, 34), x, y)

        skill.update(screen, mouse_pressed, (mouse_x, mouse_y), obj_blit, x, screen_width)

        pygame.display.flip()
