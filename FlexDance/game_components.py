# This file houses classes like Screen, Button, and Arrow
class Screen (object):
    def __init__(self, name):
        self.name = name
        pass

    def draw(self):
        # draw the things for this screen
        pass

    def left_arrow_click(self):
        # do something when the left arrow is clicked
        pass

    #...

class MenuScreen (Screen):
    def __init__(self, name, buttons):
        # initialize a menu
        pass

    def left_arrow_click(self):
        pass

    def right_arrow_click(self):  
        pass
