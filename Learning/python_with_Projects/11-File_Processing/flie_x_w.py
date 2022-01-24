
'''
# File creation and writing data...
    >_ "x" = Create
    >_ "w" = override and write
    >_ "r" = Read
    >_ "a" = Append

'''
    
with open("tests/forces.txt", "w") as forces:
    forces.write("\t Electromagnetism \n\t Gravity \n\t Strong & Weak forces \n ")
    forces.write("\n Dark Matter & Dark Energy \n")
    

