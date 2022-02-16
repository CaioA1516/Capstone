import pygame
import os


ARROW_OUTLINE_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_outline.png"))
ARROW_BLUE_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_blue.png"))
ARROW_PINK_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_pink.png"))
ARROW_YELLOW_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_yellow.png"))
ARROW_BROWN_IMG = pygame.image.load(os.path.join("Assets", "Arrows", "arrow_brown.png"))
UP, DOWN, LEFT, RIGHT = [90, 270, 180, 0]
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
ARROW_COLORED_DICT = {UP : ARROW_BLUE_IMG, DOWN : ARROW_PINK_IMG, LEFT : ARROW_YELLOW_IMG, RIGHT : ARROW_BROWN_IMG}


class Arrow(object):
    def __init__(self, direction, pos):
        self.direction = direction
        self.image = pygame.transform.scale(pygame.transform.rotate(ARROW_OUTLINE_IMG, direction), (90, 75)).convert_alpha()
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
        self.image = pygame.transform.scale(pygame.transform.rotate(
            ARROW_COLORED_DICT[direction], direction), (90, 75)).convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(center = pos)
        self.perfect_rect = self.image.get_rect(center = pos)
        self.perfect_rect.width = (1/5)*self.rect.width
        self.perfect_rect.height = (1/5)*self.rect.height

    def move_up(self, px):
        self.rect.top -= px
