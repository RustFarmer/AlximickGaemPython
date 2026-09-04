
class UseSkill:
    def __init__(self):
        pass

    def mouse_use(self, mouse_pressed, mouse_pos, obj_blit):
        if mouse_pressed[0]:
            if mouse_pressed[0] and obj_blit.collidepoint(mouse_pos):
                return True
