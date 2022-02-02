
# building a coin object 

import random


#classes
class rupee1:

    def __init__(self, rare = False):   #constructor

        self.rare = rare

        if self.rare:
            self.value = '1.33 INR'
        else:
            self.value = '1.00 INR'

        self.colour = 'silver'

    def rust(self):
        self.colour = 'brown'

    def clean(self):
        self.colour = 'silver'

        self.diameter = '21.93 mm'
        self.thickness = '1.45 mm'
        self.mass = '3.76 grams'
        self.edges = 3
        self.heads = True

    def flip(self):
        results = [True, False]
        output = random.choice(results)      #random.choice
        self.heads = output


    def __del__(self):               #destructor
        print("Coin Speant !")




coin1 = rupee1()

# normal & rare coin
print(coin1.value)
coin1 = rupee1(rare = True)
print(coin1.value)


print(coin1.colour)
coin1.rust()
print(coin1.colour)
coin1.clean()
print(coin1.colour)


coin1.flip()
print('heads;',coin1.heads)


del coin1       #destruct the coin1
























'''
# objects

coin1 = rupee1()

# print(type(coin1))

print('value;',coin1.value)
print('colour;',coin1.colour)
print('mass;',coin1.mass)

coin1.colour = 'brownish'    # Updating the object
print('rusted coin colour;',coin1.colour)    

coin2 = rupee1()
print('coin2 colour;',coin2.colour)     # Every object has it's own property

'''




