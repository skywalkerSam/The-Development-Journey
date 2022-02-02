
# *args  &  **kwargs
    #-> args = arguments  &  kwargs = keyword arguments


list1=['sahil','murlidhar','captian','ms',33,66,99]
print(list1)
print(*list1)      #packing    #args(*)

dict1={'sahil':'simple','murlidhar':'complex and little confused','captainms':'knows what is life and where the future is !','numbers':369}
print(dict1)
print(*dict1)     #packing    #args(*)




#multi number add in simple two number adding function, using args which packs the arguments

def add(x,y):
    add1=x+y
    return add1

out1=add(3,6)
print(out1)

def add(*numbers):        
    total=0
    for number in numbers:
        total=total+number
    return(total)

out2=add(3,6,9,33,66,99)
print(out2)

    


#kwargs(**)

dictonary1={'name':'CaptainMS','age':'15','like':'programming and space technologies'}
# print(dictonary1)

def about(name,age,like):
    sentence='The username is {}! his age is {} years and he likes {}'.format(name,age,like)
    return sentence

output1=about(**dictonary1)      #kwargs(**)
print(output1)


    

#packing into dictonary{}

def pack_in_dict(**dictionary2):
    for key,value in dictionary2.items():
        output3='name is {} & sex is {}'.format(key,value)
        print(output3)

pack_in_dict(Murlidhar ='Male',Trisha='Female')








