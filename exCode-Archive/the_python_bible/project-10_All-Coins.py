
# Building all coins 


#importing module
import random


#classes   #parent class
class coin:   #ultimate coin class/template
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):   #constructors   #packing into dict{}

        #getting and printing values
        for key, value in kwargs.items():
            setattr(self, key, value)

        #defining values
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
        
        # rare coin
        if self.is_rare:
            self.value = self.original_value * 1.33   #value increased by 33%
        else:
            self.value = self.original_value

        # coin colour
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):   #rust
        self.colour = self.rusty_colour

    def clean(self):   #clean
        self.colour = self.clean_colour

    def __del__(self):   #destructor
        print('Coin Spent !')

    def flip(self):
        results = [True, False]
        output = random.choice(results)   #random.choice
        self.heads = output

    def __str__(self):
        return "{} coin".format(coins)



#classs   
class rupee1(coin):   #rupee1
    def __init__(self):   #constructor
        data = { 
            'original_value':1.00,
            'clean_colour':'silver',
            'rusty_colour':'brownish',
            'edges':'3',
            'diameter':'21.93 mm',
            'thickness':'1.45 mm',
            'mass':'3.76 grams'
        }

        super().__init__(**data)        #constructor   #data unpacking   #kwargs


class rupee2(coin):   #rupee2
    def __init__(self):   #constructor
        data = { 
            'original_value':2.00,
            'clean_colour':'silver',
            'rusty_colour':'brownish',
            'edges':'3',
            'diameter':'25 mm',
            'thickness':'1.54 mm',
            'mass':'4.5 grams'
        }

        super().__init__(**data)        #constructor   #data unpacking   #kwargs


class rupee5(coin):   #rupee5
    def __init__(self):   #constructor
        data = { 
            'original_value':5.00,
            'clean_colour':'gold',
            'rusty_colour':'blackish',
            'edges':'3',
            'diameter':'23 mm',
            'thickness':'1.9 mm',
            'mass':'6 grams'
        }

        super().__init__(**data)        #constructor   #data unpacking   #kwargs

    #self cleaning
    def rust(self):
        self.colour = self.clean_colour
    
    def clean(self):
        self.colour = self.clean_colour






coins = [rupee1(), rupee2(), rupee5()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.edges, coin.mass, coin.diameter, coin.thickness]
    output = "{} - colour; {}, value; {}, edges; {}, mass; {}, diameter; {}, thickness; {} ".format(*arguments)
    print(output)
















'''
#objects

coin1 = rupee1()

#colour coin1
print('colour;',coin1.colour)
coin1.rust()
print(coin1.colour,'\n')

#value coin1
print('value;', coin1.value)
# coin1 = rupee1(rare = True)
print(coin1.value,'\n')

coin2 = rupee2()

#colour coin2
print('colour;',coin2.colour)
coin2.rust()
print(coin2.colour,'\n')

#value coin2
print('value;', coin2.value)
# coin2 = rupee2(rare = True)
print(coin2.value,'\n')

coin5 = rupee5()

#colour coin5
print('colour;',coin5.colour)
coin5.rust()
print(coin5.colour,'\n')

#value coin5
print('value;', coin5.value)
# coin5 = rupee2(rare = True)
print(coin5.value,'\n')


'''



