 
# get data from user
actual_inp = input('Enter data to encrypt ; ').strip().lower()


# split it into individual words
data_inpt = actual_inp.split()


# encryption
enctd_data = []

for vowel_inp in data_inpt:
    # if starts with vowel add 'yay'
    if vowel_inp[0] in 'aeiou':
        data_new = vowel_inp + 'yay'                         # Don't change the original data, just create a new variable similarly !
        enctd_data.append(data_new)

    # if starts with consonent add 'ay'
    else:
        cons_data = vowel_inp + 'ay'
        enctd_data.append(cons_data)

# print(enctd_data)
 

# combine words back 
output = " ".join(enctd_data)                                 # join function()


# give Encrypted data to user
print(output)


# print(type(output))
# print(type(enctd_data))





