
# return & print() are two different things, print() only prints the value.


def sum(a,m):        #parameters
    return a+m

output=sum(3,6)      #arguments
print(output)


word='laptop'
print(word)
print(word[::-1])



# Opposite data program

data=input('Enter data : ')

def opposite(data):
    return data[::-1]                  # function() should must return 

data_out=opposite(data)
print('The opposite of your given data ; ', data_out)




