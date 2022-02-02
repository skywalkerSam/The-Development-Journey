
# vowel and consonants count program

print('\nWelcome to Vowels & Consonants counting program !')

words = input('Enter word; ').strip().lower()
vowels=0
consonants=0


# Don't change the original data, just create a new variable similarly !

for word in words:
    print(word)
    if word in 'aeiou':
        vowels = vowels+1

    else:
        consonants=consonants+1

print('Vowels = {} & Consonants = {} in your given word.'.format(vowels, consonants))
print('\nThanks For Coming :)')


