
# List Comprehension

# x in range(1,100) means x redirects on range(1,100)

# (%) gives remainder after division while (/) gives quotient


print('Even Numbers; ')
even_numbers=[x for x in range(1, 100)if x%2 == 0]
print(even_numbers)



print('Odd Numbers; ')
odd_numbers=[y for y in range(1, 100)if y%2 != 0]
print(odd_numbers)







words = ['hello', 'world', 'captainMS']
answers = [[w.lower(), w.upper(), len(w)]for w in words]
print(answers)



words = ['hello', 'world', 'captainMS']
answers = [[words.lower(), words.upper(), len(words)] for words in words]
print(answers)





