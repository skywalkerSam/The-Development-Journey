# module random's choice() function

from random import choice


questions = ['What Is Life? ; ', 'Why We Are On This Earth? ; ','Why This Universe? ; ','What Are We Actually? ; ']

question = choice(questions)

answer = 'just because'

print('\nHey, Could You Tell Me The Answer Of My Questions_\n')

user = input(question).strip()


while user != answer:
    user = input('But Why? ; ')
    

print('Okay, I Understood!\n')

