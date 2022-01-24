
# Dictonary
    # ->It stores key and it's values like a normal dictonary does.



dict1 = {}

dict1 = {"murlidhar":15, 'thinkpad':'about 6 months', 1:'99/99', }

print(type(dict1))

print(dict1)

print(dict1[1])

print(dict1["murlidhar"])

dict1['sahil'] = 'murlidhar'
print(dict1)

del dict1['sahil']
print(dict1)

# .remove function did not works in dict{}

print(dict1.keys())

print(dict1.items())

print(dict1.values())

# print(dict1[0])

print(dict1['murlidhar'])

# index did not works in dict{} , it works in list[] and tuple()



list_typecasted = list(dict1)

print(type(dict1))

print(type(list_typecasted))

print(list_typecasted[0])

print(list_typecasted[1])







# Dictonary_2
    # -> It is mainly used in databases



# list[] in dict{}

asai_team_1 = {"murlidhar":[1, 15, 'A'], 'sahil':[2, 12, 'B'], }    # it can't 002 or 001 why?

print(type(asai_team_1))

print(asai_team_1)

print(asai_team_1['murlidhar'][2])    # index because it is list[] now.

print(asai_team_1['sahil'][2])



# dict{} in dict{}

asai_team_2 = {'murlidhar':{'ID':'001', 'Age':'15', 'Grade':'A'}, 'sahil':{'ID':'002', 'Age':'12', 'Grade':'B'}, 
    'thinkpad':{'ID':'003', 'Age':'6 Months', 'Grade':'A'}}

print(asai_team_2)

print('Murlidhar,', asai_team_2['murlidhar']['ID'], asai_team_2['murlidhar']['Age'], asai_team_2['murlidhar']['Grade'])

print('Sahil,', '\tID-', asai_team_2['sahil']['ID'], '\tAge-', asai_team_2['sahil']['Age'], '\tGrade-', asai_team_2['sahil']['Grade'])


del asai_team_2['thinkpad']
print(asai_team_2)


print(type(asai_team_2))


asai_team_2['lenovo thinkpad'] = {'lifespan':'6 months', 'price':'43,000 INR'}
print(asai_team_2)

print('Lenovo Thinkpad E14, ', asai_team_2['lenovo thinkpad']['price'], asai_team_2['lenovo thinkpad']['lifespan'])
