# This file houses classes like Screen, Button, and Arrow

import pygame
import os
from sys import exit
import constants

pygame.font.init()
text = pygame.font.Font("../flex_dance/fonts/Aldrich-Regular.ttf",constants.FONT_SIZE)
text_small = pygame.font.Font("../flex_dance/fonts/Aldrich-Regular.ttf",constants.FONT_SMALL)
text_med = pygame.font.Font("../flex_dance/fonts/Aldrich-Regular.ttf",constants.FONT_MED)
WIDTH, HEIGHT = 1440, 1024
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

class Screen (object):
    def __init__(self, name):
        self.name = name

class Song (object):
    # each song will have a name, an artist, and an album cover image
    def __init__(self,name,artist,imagePath):
        self.name = name
        self.artist = artist
        self.imagePath = imagePath

class RectBoi(object):
    def __init__(self,index,startX,startY,rectcolor,imagePath,songName,artist):
        self.index = index
        self.startX = startX
        self.startY = startY
        self.rectcolor = rectcolor
        self.imagePath = imagePath
        self.songName = songName
        self.artist = artist

rect0 = RectBoi(0,486,77,(234,209,111),"../flex_dance/images/low_55.png","Low", "Flo Rida") # new
rect1 = RectBoi(1,536,224,(251,235,141),"../flex_dance/images/dj_75.png","DJ got us fall..", "Usher")
rect2 = RectBoi(2,606,404,(245,201,184),"../flex_dance/images/uptown_funk.jpg","Uptown Funk", "Bruno Mars")
rect3 = RectBoi(3,536,633,(126,176,249),"../flex_dance/images/dynamite_75.png","Dynamite", "Taio Cruz")
rect4 = RectBoi(4,486,813,(4,136,96),"../flex_dance/images/hips_dont_lie_55.png","Hips don't lie", "Shakira") # new
rectList = [rect0,rect1,rect2,rect3,rect4]
chosenSong = ["None","None"]

# load two transparent rectangle images
farthestRect = pygame.image.load("../flex_dance/images/farthestRect.png")
farthestRect = pygame.transform.scale(farthestRect, (275,116))

mediumRect = pygame.image.load("../flex_dance/images/mediumRect.png")
mediumRect = pygame.transform.scale(mediumRect, (349,148))


def moveRectUp(currX, currY, num):
    if (num == 1):
        translateX = 50
        translateY = 147
        currX += translateX
        currY += translateY

    elif (num == 2):
        translateX = 70
        translateY = 180
        currX += translateX
        currY += translateY

    elif (num == 3):
        translateX = 70
        translateY = 229
        currX -= translateX
        currY += translateY

    elif (num == 4):
        translateX = 50
        translateY = 180
        currX -= translateX
        currY += translateY
    return currX,currY

# move rect down boi trial
def moveRectDown(currX, currY, num):
    if (num == 1):
        translateX = 50
        translateY = 147
        currX -= translateX
        currY -= translateY

    elif (num == 2):
        translateX = 70
        translateY = 180
        currX -= translateX
        currY -= translateY

    elif (num == 3):
        translateX = 70
        translateY = 229
        currX += translateX
        currY -= translateY

    elif (num == 4):
        translateX = 50
        translateY = 180
        currX += translateX
        currY -= translateY
    return currX,currY


class trialScreen(Screen):
    def __init__(self,name):
        self.name = name

    def songChoice(self,name): # store selected song
        self.name = name

    def on_up_key(self):
        for i in range(len(rectList)):
            rectList[i].index += 1
            rectList[i].startX , rectList[i].startY = moveRectUp(rectList[i].startX,rectList[i].startY,rectList[i].index) #replace

    def on_down_key(self):
        for i in range(len(rectList)):
            rectList[i].startX , rectList[i].startY = moveRectDown(rectList[i].startX,rectList[i].startY,rectList[i].index) #replace
            rectList[i].index -= 1

    def clear(self):
        bg_image = pygame.image.load("../flex_dance/images/bg_image.png")
        bg_image = pygame.transform.scale(bg_image, (1440, 1024))
        WIN.blit(bg_image, (0,0))

    def removeRect(self):
        pass

    def draw(self):
        bg_image = pygame.image.load("../flex_dance/images/bg_image.png")
        bg_image = pygame.transform.scale(bg_image, (1440, 1024))
        WIN.blit(bg_image, (0,0))
        for i in range(len(rectList)):
            currColor = (rectList[i]).rectcolor
            currX = (rectList[i]).startX
            currY = (rectList[i]).startY

            if (rectList[i].index == 0 or rectList[i].index == 4): # smallest edge rectangles
                # pygame.draw.rect(WIN, constants.GREY_TRANSPARENT, pygame.Rect(currX,currY,275,116))

                # ADDING NEW AND COMMENTING UP
                WIN.blit(farthestRect, (currX,currY))

                image1     = pygame.image.load(rectList[i].imagePath)
                image1     = pygame.transform.scale(image1, (106, 106))
                songName   = text_small.render(rectList[i].songName,1,constants.BLACK)
                songArtist = text_small.render(rectList[i].artist,1,constants.BLACK)

                if (rectList[i].index == 0):
                    WIN.blit(image1, (490,83)) #add numbers to constants.py
                    WIN.blit(songName,(610,102))
                    WIN.blit(songArtist,(610,135))
                else:
                    WIN.blit(image1, (490,819)) #add numbers to constants.py
                    WIN.blit(songName,(610,838))
                    WIN.blit(songArtist,(610,871))
            
            elif (rectList[i].index == 1 or rectList[i].index == 3): # middle rectangles
                # pygame.draw.rect(WIN, constants.GREY_MEDIUM, pygame.Rect(currX,currY,349,148))

                # ADDING NEW AND COMMENTING UP
                WIN.blit(mediumRect, (currX,currY))

                image2 = pygame.image.load(rectList[i].imagePath)
                image2 = pygame.transform.scale(image2, (132, 132))
                songName   = text_med.render(rectList[i].songName,1,constants.BLACK)
                songArtist = text_med.render(rectList[i].artist,1,constants.BLACK)
                if (rectList[i].index == 1):
                    WIN.blit(image2, (543,233)) #add numbers to constants.py
                    WIN.blit(songName,(691,265))
                    WIN.blit(songArtist,(691,298))
                else:
                    WIN.blit(image2, (543,642)) #add numbers to constants.py
                    WIN.blit(songName,(691,675))
                    WIN.blit(songArtist,(691,708))
            
            elif (rectList[i].index == 2): # current selection
                pygame.draw.rect(WIN, constants.GREY_MAIN, pygame.Rect(currX,currY,468,198),0,5,5,5,5)
                image3 = pygame.image.load(rectList[i].imagePath)
                image3 = pygame.transform.scale(image3, (180, 180))
                songName   = text.render(rectList[i].songName,1,constants.BLACK)
                songArtist = text.render(rectList[i].artist,1,constants.BLACK)
                WIN.blit(image3, (616,414)) #add numbers to constants.py
                WIN.blit(songName,(811,454))
                WIN.blit(songArtist,(811,510))

        #text display
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

def confirmSong():
    for i in range(len(rectList)):
        print(rectList[i].index)
        if (rectList[i].index == 2):
            chosenSong[0] = rectList[i].songName
            chosenSong[1] = rectList[i].artist

class nextTrialScreen(Screen):
    def __init__(self,name):
        self.name = name
    
    def draw(self):
        pygame.draw.rect(WIN, (234,234,234), pygame.Rect(0, 0, 1024, 1140))
        songChoice = text.render("Chosen song is",1,constants.BLUE) # confirm if song selection is correct
        songNamefinal = text.render(chosenSong[0],1,constants.BLUE)
        WIN.blit(songChoice,(85,430))
        WIN.blit(songNamefinal,(100,450))
    
    def clear(self):
        pygame.draw.rect(WIN, (234,234,234), pygame.Rect(0, 0, 1024, 1140))

