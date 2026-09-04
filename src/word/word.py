import pygame
from src.character.RedyPlayer import Player
from src.character.Skill.drawSkillIcon.drawSkillIcon import DrawSkillButton


def word(program_name, runner):
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(program_name)
    background_image = pygame.image.load('static/image/af.png')
    s = screen.get_width()
    ss = screen.get_height()
    print(screen.get_width(), screen.get_height())
    print(type(pygame.FULLSCREEN), pygame.FULLSCREEN, type(ss))

    while runner:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False

        screen.blit(background_image, (-1, -1))
        Player().draw_player(screen, (255, 100, 34), 30, 30)
        screen.blit(DrawSkillButton().draw_button_skill(), (1800, 900))
        pygame.display.flip()
