'''
blob attributes
blob = {
    color: [R,G,B],
    color_name: 'name',
    ideal: [R,G,B],
    position: [X, Y, angle],
    happiness: value,
    connectors: [angle, type],

blob external functions
    blob.attraction_to(another_blob)
}
'''

import random

class blob (object):
    '''defines blobs'''

    #this looks like something for a config file
    color_list = [
        [255, 255, 255,'white'],
        [0, 0, 0, 'black'],
        [255, 0, 0, 'red'],
        [0, 255, 0, 'green'],
        [0, 0, 255, 'blue'],
        #more!
    ]

    feelings = [
        'is ambivalent towards',
        'knows a bit about',
        'sort of likes',
        'feels friendly towards',
        'has quite a bit of affection for',
        'is in love with',

    ]

    relationships = [
        'is on good terms with',
        'is friends with',
        'is good friends with',
        'is best friends with',
        'is dating',
        'is in love with',
        'is soul bonded to',
    ]

    def __init__ (self):
        R = 0; G = 1; B = 2

        color = blob.color_list[random.randrange(0,len(blob.color_list))]
        self.color = [color[R], color[G], color[B]]
        self.color_name = color[3]

        self.ideal = [self.ideal_R(), self.ideal_G(), self.ideal_B()]

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

    def attraction_to (self, other):
        '''
        determines attraction of this blob to another blob
        Input:
            blob object
        Output:
            attraction constant (0 ~ 100)
        '''
        R = 0; G = 1; B = 2
        diff_R = abs(self.ideal[R] - other.color[R])
        diff_G = abs(self.ideal[G] - other.color[G])
        diff_B = abs(self.ideal[B] - other.color[B])
        sum_diff = diff_R + diff_G + diff_B
        attraction = (768 - sum_diff)*100/768
        return attraction

    def affection_for (self, other):

if __name__ == '__main__':
    a = blob()
    b = blob()
    c = blob()
    d = blob()
    e = blob()
