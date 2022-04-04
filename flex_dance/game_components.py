# This file houses classes like Screen, Button, and Arrow

import pygame
import os
from sys import exit
import constants


pygame.font.init()
text = pygame.font.Font("../flex_dance/fonts/Aldrich-Regular.ttf",30)

WIDTH, HEIGHT = 1440, 1024
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

class Screen (object):
    def __init__(self, name):
        self.name = name
        # pass

    # def draw(self):
    #     # draw the things for this screen
    #     pass

    # def left_arrow_click(self):
    #     # do something when the left arrow is clicked
    #     pass

    #...

class MenuScreen (Screen):
    def __init__(self,name):
        self.name = name
        # pass

    def up_arrow_click(self):
        pass

    def down_arrow_click(self):
        pass

    def right_arrow_click(self):  
        pass
    
    def draw(self):
        # display logo
        logo = pygame.image.load("../flex_dance/images/logo_transparent.png")
        logo = pygame.transform.scale(logo, (339, 181.09))
        logox = 85
        logoy = 104
        # WIN.blit(logo, (logox,logoy))

        # display images

        #image 1
        pygame.draw.rect(WIN, constants.GREY_TRANSPARENT, pygame.Rect(486, 77, 275, 116))
        image1 = pygame.image.load(song1.imagePath)
        image1 = pygame.transform.scale(image1, (106, 106))
        x = 490
        y = 83
        WIN.blit(image1, (x,y))

        #image 2
        pygame.draw.rect(WIN, constants.GREY_MEDIUM, pygame.Rect(536, 224, 349, 148))
        image2 = pygame.image.load(song2.imagePath)
        image2 = pygame.transform.scale(image2, (132, 132))
        x = 543
        y = 233
        WIN.blit(image2, (x,y))

        #image 3
        pygame.draw.rect(WIN, constants.GREY_MAIN, pygame.Rect(606, 404, 468, 198))
        image3 = pygame.image.load(song3.imagePath)
        image3 = pygame.transform.scale(image3, (180, 180))
        x = 616
        y = 414
        WIN.blit(image3, (x,y))

        #image 4
        pygame.draw.rect(WIN, constants.GREY_MEDIUM, pygame.Rect(536, 633, 349, 148))
        image4 = pygame.image.load(song4.imagePath)
        image4 = pygame.transform.scale(image4, (132, 132))
        x = 543
        y = 642
        WIN.blit(image4, (x,y))

        #image 5
        pygame.draw.rect(WIN, constants.GREY_TRANSPARENT, pygame.Rect(486, 813, 275, 116))
        image5 = pygame.image.load(song5.imagePath)
        image5 = pygame.transform.scale(image5, (106, 106))
        x = 490
        y = 819
        WIN.blit(image5, (x,y))

        #text
        x = 85
        y = 430
        text_displayed = text.render("Instructions",1,constants.WHITE)
        WIN.blit(text_displayed,(x,y))

        y = 496
        text_displayed = text.render("Selecting music:",1,constants.BLUE)
        WIN.blit(text_displayed,(x,y))
        
        y = 536
        text_displayed = text.render("Use     to choose music",1,constants.GREY_MAIN)
        WIN.blit(text_displayed,(x,y))

        y = 576
        text_displayed = text.render("and      when ready",1,constants.GREY_MAIN)
        WIN.blit(text_displayed,(x,y))

        y = 660
        text_displayed = text.render("Game:",1,constants.BLUE)
        WIN.blit(text_displayed,(x,y))

        y = 702
        text_displayed = text.render("Input arrows using your",1,constants.GREY_MAIN)
        WIN.blit(text_displayed,(x,y))

        y = 744
        text_displayed = text.render("mat. The closest overlap",1,constants.GREY_MAIN)
        WIN.blit(text_displayed,(x,y))

        y = 786
        text_displayed = text.render("of arrows will get you",1,constants.GREY_MAIN)
        WIN.blit(text_displayed,(x,y))

        y = 828
        text_displayed = text.render("the highest points.",1,constants.GREY_MAIN)
        WIN.blit(text_displayed,(x,y))

        #arrow images in menu instructions
        arrows_image = pygame.image.load("../flex_dance/images/arrows_menu.png")
        arrows_image = pygame.transform.scale(arrows_image, (38, 89))
        x = 145
        y = 525
        WIN.blit(arrows_image, (x,y))

class Song (object):
    # each song will have a name, an artist, and an album cover image
    def __init__(self,name,artist,imagePath):
        self.name = name
        self.artist = artist
        self.imagePath = imagePath

# maybe move the following to a new file or something
song1 = Song("Low", "Flo Rida", "../flex_dance/images/low_55.png")
song2 = Song("DJ got us falling in love again", "Usher", "../flex_dance/images/dj_75.png")
song3 = Song("Uptown Funk", "Bruno Mars", "../flex_dance/images/uptown_funk.jpg")
song4 = Song("Dynamite", "Taio Cruzs", "../flex_dance/images/dynamite_75.png")
song5 = Song("Hips don't lie", "Shakiras","../flex_dance/images/hips_dont_lie_55.png")

# songList = [song1, song2, song3, song4, song5]



