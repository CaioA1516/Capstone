# This file runs the main game loop for FlexDance 

# Import standard modules
import pygame
import os
from sys import exit

pygame.font.init()

# Import our modules
from game_components import MenuScreen
from trial import trialScreen
from trial import nextTrialScreen
import trial
import constants

# initialize the screen
WIDTH, HEIGHT = 1440, 1024
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WIN.fill(constants.BLACK)  
pygame.display.set_caption("Flex Dance")

pygame.init()

bg_image = pygame.image.load("../flex_dance/images/bg_image.png")
bg_image = pygame.transform.scale(bg_image, (1440, 1024))
WIN.blit(bg_image, (0,0))

def close_game():
    pygame.quit()
    exit()

def main():
    run = True
    # current_screen = MenuScreen("Menu")
    current_screen = trialScreen("Menu")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP):
                    current_screen.on_up_key()
                
                elif (event.key == pygame.K_DOWN):
                    current_screen.on_down_key()
                
                elif (event.key == pygame.K_RIGHT):
                    current_screen = nextTrialScreen("Menu")
                    trial.confirmSong()
                    final_song = trial.chosenSong[0]
                    print(final_song)
        
        # current_screen.clear()
        current_screen.draw()
         
        pygame.display.update()

main()








########################


            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            #     current_screen.left_arrow_click()
            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            #     current_screen.right_arrow_click()
            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            #     current_screen.up_arrow_click()
            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            #     current_screen.down_arrow_click()
            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
            #     current_screen.pause_click()
            # if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            #     current_screen.submit_click()

            # add more events if needed

        # # Update the screen
        # current_screen.update()

        # # Draw the screen
        # current_screen.draw()