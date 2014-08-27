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
        [255, 255, 255,'pure white'],
        [0, 0, 0, 'pure black'],
        [255, 0, 0, 'pure red'],
        [0, 255, 0, 'pure green'],
        [0, 0, 255, 'pure blue'],
        [218, 165, 32, 'golden rod'],
        [245, 222, 179, 'wheat'],
        [255, 127, 80, 'coral'],
        [139, 69, 19, 'chocolate'],
        [0, 100, 0, 'darkgreen'],
        [240, 255, 240, 'honeydew'],
        [128, 0, 128, 'purple']
        #more!
    ]

    feelings = [
        'is ambivalent towards',
        'knows a bit about',
        'sort of likes',
        'feels friendly towards',
        'has quite a bit of affection for',
        'is in love with',
        #more!
    ]

    relationships = [
        'doesnt feel much towards',
        'is on good terms with',
        'is friends with',
        'is good friends with',
        'is best friends with',
        'is dating',
        'is in love with',
        'is soul bonded to',
        #more!
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
        '''
        return (-self.color[0]+255)

    def ideal_G (self):
        '''
        green is gay, attraction to colors like yourself
        the more green you are, the more you are attracted to green
        '''
        return (self.color[1])

    def ideal_B (self):
        '''
        blue is pansexuality, attraction to all colors
        the more color you have, the more you are attracted to blue
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
        print(str(self.color_name)+' has '+str(attraction)+' to '+str(other.color_name))
        return attraction

    def affection_for (self, other):
        pass

    def relationship_with (self, other):
        pass

if __name__ == '__main__':
    a = blob()
    b = blob()
    c = blob()
    d = blob()
    e = blob()
    f = blob()
    g = blob()
    ae = [a,b,c,d,e,f,g]
    print(a.ideal)
    for thing in ae:
        a.attraction_to(thing)
