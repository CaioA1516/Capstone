from distutils.command.build import build
from tkinter.tix import TEXT
from matplotlib.pyplot import arrow
import pygame
import os
import arrows
from random import choice
from sys import exit
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 1 mini-project")

BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.jpg'))

FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_GREY = (200, 200, 200)

STATIONARY_ARROWS_HEIGHT = HEIGHT * (1/10) 
NEW_ARROW_SPAWN_INTERVAL = 1000 # miliseconds
ARROW_VEL = 5 # 5 pixels / second
SPAWN_ARROW_EVENT = pygame.USEREVENT + 1

INC_VEL = pygame.USEREVENT + 2
INC_VEL_INTERVAL = 7000 # milliseconds
INC_VEL_RATE = 1.5

FONT_SIZE = 50
GAME_OVER_SIZE = 30
TEXT_FONT = pygame.font.Font(os.path.join("Assets", "Font", "BalonkuRegular-la1w.otf"), FONT_SIZE)
GAME_OVER_FONT = pygame.font.Font(os.path.join("Assets", "Font", "BalonkuRegular-la1w.otf"), GAME_OVER_SIZE)

# End pygame and immediately end program
def close_game():
    pygame.quit()
    exit()

# Create the stationary arrows on the top of the screen
def build_stationary_arrows(height):
    stationary_arrows = list()
    for direction in arrows.DIRECTIONS:
        if direction == arrows.LEFT:
            pos = (WIDTH * (1/15), height)
        elif direction == arrows.DOWN:
            pos = (WIDTH * (3/15), height)
        elif direction == arrows.UP:
            pos = (WIDTH * (5/15), height)
        elif direction == arrows.RIGHT:
            pos = (WIDTH * (7/15), height)

        stationary_arrows.append(arrows.Arrow(direction, pos))
    
    return stationary_arrows

def move_arrows(m_arrows, vel):
    arrows_to_remove = []
    life_dec = 0
    for arrow in m_arrows:
        arrow.move_up(vel)
        if arrow.get_rect().bottom < 0:
            arrows_to_remove.append(arrow)

    for arrow in arrows_to_remove:
        m_arrows.remove(arrow)
        life_dec += 1

    return life_dec

def draw(s_arrows, m_arrows, score, lives):
    WIN.blit(BACKGROUND, (0,0))
    for arrow in s_arrows:
        arrow.draw(WIN)

    for arrow in m_arrows:
        arrow.draw(WIN)

    # draw the score & lives
    score_surface = TEXT_FONT.render("Score: " + str(score), True, BLACK)
    score_rectangle = score_surface.get_rect(center = ((3/4)*WIDTH, (2/4)*HEIGHT))
    WIN.blit(score_surface, score_rectangle)

    # draw lives left
    lives_surface = TEXT_FONT.render("Lives: " + str(lives), True, BLACK)
    lives_rectangle = lives_surface.get_rect(center = ((3/4)*WIDTH, (5/8)*HEIGHT))
    WIN.blit(lives_surface, lives_rectangle)

def handle_arrow_key_pressed(key, s_arrows, m_arrows):
    score_inc = 0
    arrows_to_remove = []
    for arrow in m_arrows:
        if (key == pygame.K_UP and arrow.direction != arrows.UP) or\
           (key == pygame.K_DOWN and arrow.direction != arrows.DOWN) or\
           (key == pygame.K_LEFT and arrow.direction != arrows.LEFT) or\
           (key == pygame.K_RIGHT and arrow.direction != arrows.RIGHT):
            continue
                
        for s_arrow in s_arrows:
            if arrow.get_perfect_rect().colliderect(s_arrow.get_perfect_rect()):
                score_inc += 10
                arrows_to_remove.append(arrow)
            elif arrow.get_rect().colliderect(s_arrow.get_rect()):
                score_inc += 5
                arrows_to_remove.append(arrow)

        for arrow in arrows_to_remove:
            if arrow in m_arrows:
                m_arrows.remove(arrow)

    return score_inc
    

def main():

    run = True
    clock = pygame.time.Clock()
    pygame.time.set_timer(SPAWN_ARROW_EVENT, NEW_ARROW_SPAWN_INTERVAL)
    pygame.time.set_timer(INC_VEL, INC_VEL_INTERVAL)

    stationary_arrows = build_stationary_arrows(STATIONARY_ARROWS_HEIGHT)
    moving_arrows = list()
    score = 0
    lives = 3
    arrow_vel = ARROW_VEL
    game_active = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            
            if game_active:
                if event.type == SPAWN_ARROW_EVENT:
                    new_direction = choice(arrows.DIRECTIONS)
                    if new_direction == arrows.LEFT:
                        pos = (WIDTH * (1/15), HEIGHT)
                    elif new_direction == arrows.DOWN:
                        pos = (WIDTH * (3/15), HEIGHT)
                    elif new_direction == arrows.UP:
                        pos = (WIDTH * (5/15), HEIGHT)
                    elif new_direction == arrows.RIGHT:
                        pos = (WIDTH * (7/15), HEIGHT)

                    moving_arrows.append(arrows.MovingArrow(new_direction, pos))

                if event.type == INC_VEL:
                    arrow_vel *= INC_VEL_RATE
                    if arrow_vel > 9:
                        pygame.time.set_timer(INC_VEL, 0)

            if event.type == pygame.KEYDOWN:
                if game_active and event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
                    score += handle_arrow_key_pressed(event.key, stationary_arrows, moving_arrows)
                
                if not game_active:
                    run = False

        if game_active:
            # update things
            lives -= move_arrows(moving_arrows, arrow_vel)
            
            # draw things
            draw(stationary_arrows, moving_arrows, score, lives)

        if lives <= 0:
            game_active = False

        if not game_active:
            pygame.draw.rect(WIN, LIGHT_GREY, 
                             pygame.rect.Rect((1/6)*WIDTH, (1/4)*HEIGHT, (2/3)*WIDTH, (1/3)*HEIGHT))

            game_over_surface = GAME_OVER_FONT.render("Game Over!", True, BLACK)
            game_over_rectangle = game_over_surface.get_rect(center = ((1/2)*WIDTH, (3/8)*HEIGHT))
            WIN.blit(game_over_surface, game_over_rectangle)
            game_over_surface = GAME_OVER_FONT.render("Press any key to restart...", True, BLACK)
            game_over_rectangle = game_over_surface.get_rect(center = ((1/2)*WIDTH, (1/2)*HEIGHT))
            WIN.blit(game_over_surface, game_over_rectangle)

        pygame.display.update()

    main()

if __name__ == "__main__":
    main()