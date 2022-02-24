# This file runs the main game loop for FlexDance 

# Import standard modules
import pygame
import os
from sys import exit

# Import our modules
from game_components import MenuScreen

pygame.init()

def close_game():
    pygame.quit()
    exit()

def main():
    run = True
    current_screen = MenuScreen("my menu", [1,2,3])

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                current_screen.left_arrow_click()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                current_screen.right_arrow_click()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                current_screen.up_arrow_click()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                current_screen.down_arrow_click()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
                current_screen.pause_click()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                current_screen.submit_click()

            # add more events if needed

        # Update the screen
        current_screen.update()

        # Draw the screen
        current_screen.draw()