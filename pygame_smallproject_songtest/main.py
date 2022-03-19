from distutils.command.build import build
from tkinter.tix import TEXT
from matplotlib.pyplot import arrow
from zipfile import ZipFile
import pyautogui # for some reason this fixes 4K scaling issues
import pygame
import os
import time
import arrows
from random import choice
from sys import exit
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Retrieve monitor resolution
# infoObject = pygame.display.Info()
# WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
WIDTH, HEIGHT = 3840, 2160
print(WIDTH, HEIGHT)
# print(pygame.display.list_modes())
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Flex Dance game screen")

BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Background", 'starry_sky.png')), (WIDTH, HEIGHT)).convert_alpha()
BANNER = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Background", 'banner.png')), ((413 / 1440) * WIDTH, (40.46 / 1080) * HEIGHT)).convert_alpha()
BANNER_POS = ((89 / 1440) * WIDTH, (61 / 1080) * HEIGHT)

FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_GREY = (200, 200, 200)

STATIONARY_ARROWS_HEIGHT = (302.44 / 1080) * HEIGHT 

SPAWN_LEFT_ARROW_EVENT = pygame.USEREVENT + 1
SPAWN_UP_ARROW_EVENT = pygame.USEREVENT + 2
SPAWN_DOWN_ARROW_EVENT = pygame.USEREVENT + 3
SPAWN_RIGHT_ARROW_EVENT = pygame.USEREVENT + 4

SONG_ICON_POS = ((1043 / 1440) * WIDTH, (720 / 1080) * HEIGHT)
SONG_ICON_DIM = ((268 / 1440) * WIDTH, (268 / 1440) * WIDTH)

FONT_SIZE = 50
GAME_OVER_SIZE = 30
TEXT_FONT = pygame.font.Font(os.path.join("Assets", "Font", "BalonkuRegular-la1w.otf"), FONT_SIZE)
GAME_OVER_FONT = pygame.font.Font(os.path.join("Assets", "Font", "BalonkuRegular-la1w.otf"), GAME_OVER_SIZE)

SEGMENTS_PER_MEASURE = 16.0

# End pygame and immediately end program
def close_game():
    pygame.mixer.music.stop()
    pygame.quit()
    exit()

# Create the stationary arrows on the top of the screen
def build_stationary_arrows(height):
    stationary_arrows = list()
    for direction in arrows.DIRECTIONS:
        if direction == arrows.LEFT:
            pos = (WIDTH * (202.52 / 1440), height)
        elif direction == arrows.UP:
            pos = (WIDTH * (378.22 / 1440), height)
        elif direction == arrows.DOWN:
            pos = (WIDTH * (564.22 / 1440), height)
        elif direction == arrows.RIGHT:
            pos = (WIDTH * (723.52 / 1440), height)

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

def draw(s_arrows, m_arrows, score, lives, song_icon):
    WIN.blit(BACKGROUND, (0,0))
    WIN.blit(BANNER, BANNER_POS)
    WIN.blit(song_icon, SONG_ICON_POS)

    for arrow in s_arrows:
        arrow.draw(WIN)

    for arrow in m_arrows:
        arrow.draw(WIN)

    # draw the score & lives
    score_surface = TEXT_FONT.render("Score: " + str(score), True, WHITE)
    score_rectangle = score_surface.get_rect(center = ((3/4)*WIDTH, (2/4)*HEIGHT))
    WIN.blit(score_surface, score_rectangle)

    # draw lives left
    lives_surface = TEXT_FONT.render("Lives: " + str(lives), True, WHITE)
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

def raise_spawn_arrow(arrow_direction): 
    if arrow_direction == arrows.LEFT:
        pygame.event.post(pygame.event.Event(SPAWN_LEFT_ARROW_EVENT))
    elif arrow_direction == arrows.UP:
        pygame.event.post(pygame.event.Event(SPAWN_UP_ARROW_EVENT))
    elif arrow_direction == arrows.DOWN:
        pygame.event.post(pygame.event.Event(SPAWN_DOWN_ARROW_EVENT))
    elif arrow_direction == arrows.RIGHT:
        pygame.event.post(pygame.event.Event(SPAWN_RIGHT_ARROW_EVENT))
    else:
        print("Bad direction")

def arrow_sequence_extractor(arrow_sequence_path):
    arrow_sequence_file = open(arrow_sequence_path, mode='r')
    lines = arrow_sequence_file.readlines()
    lines_no_comments = []
    for line in lines:
        if line[0] != '#':
            lines_no_comments.append(line)
    measure_length = float(lines_no_comments[0])
    segment_length = measure_length / SEGMENTS_PER_MEASURE

    arrow_vel = (HEIGHT - STATIONARY_ARROWS_HEIGHT) /  (measure_length * FPS)
    """arrow_sequence = [
                        {"timestamp": 4.0, "arrows": [arrows.LEFT]},
                        {"timestamp": 5.0, "arrows": [arrows.UP]},
                        {"timestamp": 6.0, "arrows": [arrows.DOWN]},
                        {"timestamp": 7.0, "arrows": [arrows.RIGHT]},
                        {"timestamp": 8.0, "arrows": [arrows.LEFT]},
                        {"timestamp": 8.5, "arrows": [arrows.RIGHT]},
                        {"timestamp": 10.0, "arrows": [arrows.UP]},
                        {"timestamp": 10.5, "arrows": [arrows.DOWN]},
                        {"timestamp": 12.0, "arrows": [arrows.LEFT, arrows.RIGHT]},
                        {"timestamp": 14.0, "arrows": [arrows.LEFT, arrows.RIGHT]},
                        {"timestamp": 16.0, "arrows": [arrows.UP]},
                        {"timestamp": 16.5, "arrows": [arrows.RIGHT]},
                        {"timestamp": 17.0, "arrows": [arrows.DOWN]},
                        {"timestamp": 17.5, "arrows": [arrows.LEFT]},
                        {"timestamp": 18.0, "arrows": [arrows.UP]},
                        {"timestamp": 18.5, "arrows": [arrows.LEFT, arrows.RIGHT]},
    ]"""
    arrow_sequence = []
    index = 1
    while index < len(lines_no_comments):
        timestamp = (index) * segment_length
        arrows_seq = []
        added_arrow_flag = False
        line = lines_no_comments[index]

        # Check which arrows are present
        if line[0] == '1':
            arrows_seq.append(arrows.LEFT)
            added_arrow_flag = True
        if line[1] == '1':
            arrows_seq.append(arrows.UP)
            added_arrow_flag = True
        if line[2] == '1':
            arrows_seq.append(arrows.DOWN)
            added_arrow_flag = True
        if line[3] == '1':
            arrows_seq.append(arrows.RIGHT)
            added_arrow_flag = True
        
        if added_arrow_flag:
            arrow_sequence.append({"timestamp": timestamp, "arrows": arrows_seq})

        index += 1

    arrow_sequence_file.close()
    return measure_length, arrow_sequence, arrow_vel
    

def main():

    run = True
    clock = pygame.time.Clock()

    stationary_arrows = build_stationary_arrows(STATIONARY_ARROWS_HEIGHT)
    moving_arrows = list()
    score = 0
    lives = 3
    game_active = True

    current_arrow_index = 0
    # Testing the music playing part
    song_name = "into-the-night"
    folder_path = os.path.join("Assets", "Song", song_name)
    mp3_path = os.path.join(folder_path, song_name + ".mp3")
    pygame.mixer.music.load(mp3_path)

    arrow_sequence_path = os.path.join(folder_path, song_name + ".txt")
    measure_legnth, arrow_sequence, arrow_vel = arrow_sequence_extractor(arrow_sequence_path)

    song_icon = pygame.image.load(os.path.join(folder_path, song_name + "-icon.jpg"))
    song_icon = pygame.transform.scale(song_icon, SONG_ICON_DIM)

    start_time = time.time()
    song_is_playing = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            
            if game_active:
                if event.type == SPAWN_LEFT_ARROW_EVENT:
                    pos = (WIDTH * (202.52 / 1440), HEIGHT)
                    moving_arrows.append(arrows.MovingArrow(arrows.LEFT, pos))

                if event.type == SPAWN_UP_ARROW_EVENT:
                    pos = (WIDTH * (378.22 / 1440), HEIGHT)
                    moving_arrows.append(arrows.MovingArrow(arrows.UP, pos))

                if event.type == SPAWN_DOWN_ARROW_EVENT:
                    pos = (WIDTH * (564.22 / 1440), HEIGHT)
                    moving_arrows.append(arrows.MovingArrow(arrows.DOWN, pos))
                
                if event.type == SPAWN_RIGHT_ARROW_EVENT:
                    pos = (WIDTH * (723.52 / 1440), HEIGHT)

                    moving_arrows.append(arrows.MovingArrow(arrows.RIGHT, pos))

            if event.type == pygame.KEYDOWN:
                if game_active and event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
                    score += handle_arrow_key_pressed(event.key, stationary_arrows, moving_arrows)
                
                if not game_active:
                    run = False

        if game_active:
            # update things
            lives -= move_arrows(moving_arrows, arrow_vel)
            
            # check if should spawn arrows
            if current_arrow_index < len(arrow_sequence):
                current_time_passed = time.time() - start_time
                if not song_is_playing and current_time_passed >= measure_legnth:
                        pygame.mixer.music.play()
                        song_is_playing = True
                if current_time_passed >= arrow_sequence[current_arrow_index]["timestamp"]:
                    arrows_to_spawn = arrow_sequence[current_arrow_index]["arrows"]
                    for arrow in arrows_to_spawn:
                        raise_spawn_arrow(arrow)
                    current_arrow_index += 1
            """if current_arrow_index >= len(arrow_sequence):
                current_arrow_index = 0
                start_time = time.time()"""

            # draw things
            draw(stationary_arrows, moving_arrows, score, lives, song_icon)

        if lives <= 0:
            pygame.mixer.music.stop()
            song_is_playing = False
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