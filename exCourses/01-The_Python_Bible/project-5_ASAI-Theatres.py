"""
Developer: Captain Skywalker
Purpose: Project-5, ASAI Theatres
Stardate: 12020.--

"""

# shows
shows = {'The Avengers': [13],
         "The Avengers - Age Of Ultron": 13,
         "The Avengers - Civil War": 13,
         "The Avengers - Infinity War": 13,
         "The Avengers - Endgame": 13,
         "Star Trek": 13,
         'A Divergent Series': [16],
         'Iron Man': [13],
         "Iron Man 2": 13,
         "Iron Man 3": 13,
         "Black Widow": 13,
         "Shang Chi - The Legend Of Ten Rings": 13,
         "Eternals": 13,
         "Spiderman - No Way Home": 13,
         "What If..": 7,
         "Guardians Of The Galaxy": 13,
         "Transformers": 13,
         "Transformers - Revenge Of The Fallen": 13,
         "Transformers - Darkside Of The Moon": 16,
         "Transformers - Age Of Extinction": 13,
         "Transformers - The Last Knight": 18,
         "Bumblebee": 13,
         "Transformers - Rise Of The Beasts": "--",
         "Ready Player One": 16,

         }

# Total Seats
seats = 99

while True:
    # Intro
    print('\n\tWelcome To ASAI Theatres...\n\n ')

    # show name
    choice = input('Enter The Name Of The Movie\Show:  ').strip().title()

    # check for availablity
    if choice in shows:
        print('Yes, Show Available!\n')

        # ask for age
        age = int(input('Kindly Verify Your Age; '))

        # shows age limit
        show_age = shows[choice][0]

        # verify age
        if age >= show_age:
            print('Age {}, Verified!\n'.format(age))

            # update seats
            seats = seats - 1

            # verify seats
            if seats >= 0:
                print('Yehh! Seats Available.')
                print('{} Seats Left!\n'.format(seats))

                # confirmation
                username = input(
                    'Kindly Enter Your Name; ').strip().capitalize()
                print(
                    'Congratulations! {} You Can Now Watch The Show_\n'.format(username))

            # seats unavailable
            else:
                print('Sorry! Seats Unavailable.\n')

        # young error
        else:
            print('You Are Too Young For This Show!\n')

    # show Unavailable
    else:
        print('Sorry Show Unavailable!\n')
