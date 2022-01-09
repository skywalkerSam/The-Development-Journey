
#for loops

for number in range(1,1000):           # range(x,y) function
    print(number)


#function implementation
def fun1(a,b):
    for numbers in range(a,b):
        print(numbers)
    return numbers
    
fun1(1,99)
    
var1=fun1(1,333)
print(var1)




for strings in 'captainms':
    print(strings)

for str1 in 'abcdef':
    print(str1, '\n')

for num2 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(num2)

num3=[0, 1, 2, 3, 4, 5, 6, 'asai']
for num3 in num3:
    print(num3, '\n')




#for loop in dict{}

names={'male':['murlidhar','sahil','captainms','hello'],
    'female':['nimmi','trisha','khushi','ananyaa']
}

for key in names.keys():
    print(key)
    print(*names[key])                #args(*)



for key in names.keys():
    for name in names[key]:
        if 'a' in name:
            print(name)



print(names.keys())

print(names.values())

