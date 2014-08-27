'''
blob = {colors:[R,G,B]}
'''

class attract (object):
    '''defines how attracted a blob is to other blobs'''

    def __init__ (self, blob):
        R = 0; G = 1; B = 2
        self.blob = blob
        R_attract = attract_to_R(self.blob(colors(R)))
        G_attract = attract_to_R(self.blob(colors(R)))
        B_attract = attract_to_R(self.blob(colors(R)))
        self.attract(R_attract, G_attract, B_attract)

    def attract_to_R (self, R):
        '''
        Red is het, and thusly not very attracted to other reds
        Red's ideal partner is 0,255,255 == sky blue
        '''
        return (-R+255)

    def attract_to_G (self, G):
        '''
        Green is gay, and thusly attracted to other greens
        Green's ideal partner is 0,255,0 == green
        '''
        return (G)

    def attract_to_B (self, R, G, B): return 133
        '''
        Blue is pan, and is more attracted to you the more color you have
        Blue's ideal partner is 255,255,255 == black
        '''
        return ((R+G+B)/(3))
