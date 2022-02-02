
# list
    # -> list is a mutable datatype, it means it can be changed.

list1 = [3, 'ms', 13, "asai", True, False, ["list of list", '& many more datastructures'], [6203934155, 7209474037]]

print("list is; ", list1)

print(list1[3])

print(list1[6][0])

print(list1[6][:])

print(list1[-4])

print(list1[:5])



list2 = list1[1:4]

print(list2)




list1.remove(13)
print(list1)

list1.append('hello world')
print(list1)

list1.insert(0, 999)
print(list1)

list1 = list1 + [99] 
print(list1)

list1 = list1 + ['sahil'] 
print(list1)

list1 = list1 + list(['python']) 
print(list1)

list1 = list1 + list([369]) 
print(list1)


list1 = list1 + list(str('think')) 
print(list1)

list1 = list1 + list(str('333')) 
print(list1)

list1 = list1 + [[13, 23, 33, 43]]
print(list1)



list1[5] = 999999
print(list1)

del list1[5]
print(list1)







# tuple
    # -> tuple is an immutable datatype, it means it can't be changed.

tuple1 = (23, 33, 66, 99, 'hello')
print(tuple1)

(a, b, c) = 3, 6, 9 
print(a)
print(b)
print(c)

print(tuple1[0])


list3 = ['typecasting', ]
print(type(list3))

list3 = tuple(list3)
print(type(list3))
print(list3)



