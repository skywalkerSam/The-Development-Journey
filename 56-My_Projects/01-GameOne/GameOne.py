"""
    Developer: Master Skywalker
    Purpose: Game Development Project with C++
    Stardate: 12021.254.00:45:32

"""
import random


print("""
            
            "ASAI's Research Lab Is Under Attack, Break The Codes To Get Into The Datacentre Facility, Cut The Hard Line & Save The Research Data From Going Into Wrong Hands..."
            

            """)


def PlayGame():
    code_one = random.randint(1, 5)
    code_two = random.randint(1, 5)
    code_three = random.randint(1, 5)

    code_sum = code_one + code_two + code_three
    code_product = code_one * code_two * code_three

    print(">_\tHere's Some Information About The Codes...\n")
    print("+ The Total Codes:         3")
    print("+ The Codes Join Upto:    ", code_sum)
    print("+ The Codes Product Upto: ", code_product)

    guess_one = int(input("\n\n\tEnter first code:  "))
    guess_two = int(input("\tEnter second code:  "))
    guess_three = int(input("\tEnter third code:  "))

    guess_sum = guess_one + guess_two + guess_three
    guess_product = guess_one * guess_two * guess_three

    if (guess_sum == code_sum) and (guess_product == code_product):
        print("\n\t\t\t Welcome To The ASAI'S Datacentre Facility :)\n\n")
    else:
        print("\n\t\t Alert! There's A Breach In The Datacentre Facility :(\n\n")
        # print("\t Well, The Codes Were: ", code_one, code_two, code_three)
        print("\n")

level = 0
while (True):
    PlayGame()
    level=level+1
    
    continue









