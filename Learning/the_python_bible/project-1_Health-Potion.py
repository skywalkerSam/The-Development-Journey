"""
Developer: Captain Murlidhar Singh
Purpose: Project-1, Crafting a Health Potion
Stardate: 12020.--

"""

import random

health = 50

# 1=easy, 2=medium, 3=hard
difficulty_level = 1

potion_health = random.randint(25, 50) // difficulty_level
# print(potion_health)

health = health + potion_health
print("\n\tYour Current Health: ", health, "Percent\n")
