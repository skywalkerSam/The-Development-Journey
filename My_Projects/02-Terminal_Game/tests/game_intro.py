"""
Developer; Sam Skywalker
Purpose; Figlet fonts implementation in intro
Data; 12022.01.09.12:23

"""

print("""

        #################################################################
    ##########################   Terminal Game   ############################
        #################################################################

""")




from pyfiglet import *


font_one = figlet_format("Terminal Game")
print(font_one)

font_two = figlet_format("Terminal Game", font="slant")
print(font_two)

font_three = figlet_format("Terminal Game", font="script")
print(font_three)

font_four = figlet_format("Terminal Game", font="big")
print(font_four)

font_five = figlet_format("Terminal Game", font="bubble")
print(font_five)

font_six = figlet_format("Terminal Game", font="digital")
print(font_six)


