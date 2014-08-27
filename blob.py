'''
blob attributes
blob = {
    colors:[R,G,B],
    color_name: 'name',
    ideals:[R,G,B],
    position: [X, Y, angle],
    happiness: value,
    connectors: [angle, type],

blob external functions
    blob.attraction_to()
}
'''

import random

class blob (object):
    '''defines blobs'''

    #this looks like something for a config file
    color_list = [
        [255, 255, 255,'white'],
        [0, 0, 0, 'black'],
        #more!
    ]

    def __init__ (self):
        R = 0; G = 1; B = 2

        color = blob.color_list[random.randrange(0,len(blob.color_list))]
        self.color = [color[R], color[G], color[B]]
        self.color_name = color[3]

        self.ideals = [self.ideal_R(), self.ideal_G(), self.ideal_B()]

    def ideal_R (self):
        '''
        red is het, attraction to colors that are different from you
        the less red you are, the more you are attracted to red
        sky blues (0,255,255) are most attracted to reds (255,0,0)
        '''
        return (-self.color[0]+255)

    def ideal_G (self):
        '''
        green is gay, attraction to colors like yourself
        the more green you are, the more you are attracted to green
        greens (0,255,0) are most attracted to greens (0,255,0)
        '''
        return (self.color[1])

    def ideal_B (self):
        '''
        blue is pansexuality, attraction to all colors
        the more color you have, the more you are attracted to blue
        blacks (255,255,255) are most attracted to blues (0,0,255)
        '''
        return ((self.color[0]+self.color[1]+self.color[2])/(3))

    #WIP
    def attraction_to (self, other):
        R = 0; G = 1; B = 2

if __name__ == '__main__':
    b = blob()
