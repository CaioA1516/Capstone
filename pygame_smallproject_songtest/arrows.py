import pygame
import os


ARROW_OUTLINE_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_right_blank.png"))
ARROW_BLUE_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_up.png"))
ARROW_PINK_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_down.png"))
ARROW_YELLOW_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_left.png"))
ARROW_BROWN_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_right.png"))
UP, DOWN, LEFT, RIGHT = [90, 270, 180, 0]
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
ARROW_COLORED_DICT = {UP : ARROW_BLUE_IMG, DOWN : ARROW_PINK_IMG, LEFT : ARROW_YELLOW_IMG, RIGHT : ARROW_BROWN_IMG}

# These values cannot be hard coded in the end
SCREEN_WIDTH, SCREEN_HEIGHT = 3840, 2160
ARROW_WIDTH = SCREEN_WIDTH * (87.04 / 1440)
ARROW_HEIGHT = SCREEN_HEIGHT * (144.44 / 1080)

class Arrow(object):
    def __init__(self, direction, pos):
        self.direction = direction
        self.image = pygame.transform.scale(
            pygame.transform.rotate(ARROW_OUTLINE_IMG, direction), (ARROW_WIDTH, ARROW_HEIGHT)).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(center = pos)
        self.perfect_rect = self.image.get_rect(center = pos)
        self.perfect_rect.width = (1/5)*self.rect.width
        self.perfect_rect.height = (1/5)*self.rect.height

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect

    def get_perfect_rect(self):
        return self.perfect_rect

    def draw(self, window):
        window.blit(self.image, self.rect)

class MovingArrow(Arrow):
    def __init__(self, direction, pos):
        self.direction = direction
        self.image = pygame.transform.scale(ARROW_COLORED_DICT[direction], (ARROW_WIDTH, ARROW_HEIGHT)).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(center = pos)
        self.perfect_rect = self.image.get_rect(center = pos)
        self.perfect_rect.width = (1/5)*self.rect.width
        self.perfect_rect.height = (1/5)*self.rect.height

    def move_up(self, px):
        self.rect.top -= px
