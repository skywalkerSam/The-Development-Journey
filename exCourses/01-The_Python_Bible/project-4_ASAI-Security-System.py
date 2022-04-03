"""
Developer: Capt. Skywalker
Purpose: Project-4, ASAI Security System
Stardate: 12020.--

"""

# users
Registered_Users = ['Murlidhar', "Sahil", 'ASAI', 'Skywalker', "Captain"]

# password
Admin_Password = "asaiinc"

while True:
    # self-intro
    print('\n\n\t Hello,  I\'m ASAI Security System :) ...\n\n')
    # username
    username = input('Enter Your User-ID\ Username #_  ').strip().capitalize()
    # verify user
    if username in Registered_Users:
        print(
            f"\nWelcome aboard {username}, You can proceed now... \n\n")

        # ask to proceed further
        query1 = input(
            'Would you like to proceed further? (y/n); ').strip().lower()

        if query1 == 'y':
            # ask to be removed
            remove_user = input(
                'Would you like to be removed from the system? (y/n); ').strip().lower()
            if remove_user == 'y':

                # ask for the password
                Verification_Password = input(
                    'Enter The Administrator Password #_  ')

                # remove user
                if Verification_Password == Admin_Password:
                    Registered_Users.remove(username)
                    print(
                        "\nSuccessful :)  You are now removed from the registered users list...\n")

                else:
                    print('\nFailed :(  You\'ve Entered Wrong Password :( \n')
                    continue

        else:
            continue

    # if user not in list
    else:
        print('\nFailed :( I Didn\'t Recognized You :( \n\n')

        # ask to proceed further
        query2 = input(
            'Would you like to proceed further? (y/n); ').strip().lower()
        if query2 == 'y':
            # ask to be added
            update_user = input(
                'Would you like to be added to the system? (y/n); ').strip().lower()
            if update_user == 'y':
                # ask for the password
                Verification_Password = input(
                    'Enter The Administrator Password #_   ')
                # update user
                if Verification_Password == Admin_Password:
                    Registered_Users.append(username)
                    print(
                        "\nSuccessful :)  You are now added in the registered users list...\n")

                else:
                    print(
                        '\nFailed :(  You\'ve entered a wrong password, This incident will be reported :( ... \n')
                    continue

        else:
            continue
