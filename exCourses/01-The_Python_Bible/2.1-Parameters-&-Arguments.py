
def intro(name,age,like):         #parameters
    output="your name is {}, you are {} years old & you like {}".format(name,age,like)
    return output
f_output=intro('sahil',13,'python')        #arguments
print(f_output)



def intro(name,age,like='python'):         #default-parameters
    output="your name is {}, you are {} years old & you like {}".format(name,age,like)
    return output
final_output=intro(age=15,name='captain')        #keyword arguments
print(final_output)



second_output=intro('ms',16,'spacex')      #can change default parameters !
print(second_output)


# third_output= intro('16')         #you have to fulfil the parameters !
# print(third_output)


