'''
blob = {
    colors:[R,G,B],
    color_name: 'name',
    ideals:[R,G,B],
    position: ?,
    happiness: ?,
    connectors: ?,
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

    def __init__ (self, blob):
        R = 0; G = 1; B = 2
        self.blob = blob
        #init colors
        color = blob.color_list(random.randrange(0,len(blob.color_list)))
        self.color = [color[R], color[G], color[B]]
        self.color_name = color[3]
        #/colors
        #init attraction
        R_ideal = ideal_R(self.blob(colors(R)))
        G_ideal = ideal_R(self.blob(colors(G)))
        B_ideal = ideal_R(self.blob(colors(R,G,B)))
        self.ideals(R_ideal, G_ideal, B_ideal)
        #/attraction

    def ideal_R (self, R):
        '''
        red is het, attraction to colors that are different from you
        the less red you are, the more you are attracted to red
        sky blues (0,255,255) are most attracted to reds (255,0,0)
        '''
        return (-R+255)

    def ideal_G (self, G):
        '''
        green is gay, attraction to colors like yourself
        the more green you are, the more you are attracted to green
        greens (0,255,0) are most attracted to greens (0,255,0)
        '''
        return (G)

    def ideal_B (self, R, G, B):
        '''
        blue is pansexuality, attraction to all colors
        the more color you have, the more you are attracted to blue
        blacks (255,255,255) are most attracted to blues (0,0,255)
        '''
        return ((R+G+B)/(3))

    #WIP
    def attraction (self, other):
        R = 0; G = 1; B = 2
