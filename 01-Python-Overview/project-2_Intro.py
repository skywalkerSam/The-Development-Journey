"""
Developer: Captian Skywalker
Purpose: Project-2, Intro
Stardate: 12020.--

"""

# ask user for their name
name = input("\n\tEnter Your Name: ").strip().capitalize()

# ask user for their age
age = input("\tEnter Your Age: ").strip().capitalize()

# ask user for their place
place = input("\tEnter Your City\Town\Village: ").strip().capitalize()

# ask user for what they love to do
work = input("\tEnter Your Profession: ").strip().capitalize()

# create output text
logic = (
    f"\n\tHello {name}, You are {age} years old, You are from {place} & You're a {work} :)\n")
output = logic


# print output to user
print(output)
