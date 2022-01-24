
import time
import os


while (True):
    """
    In this program, Entropy's happening in every 5 secs...

    """
    if (os.path.exists("universe.txt")):
        with open("universe.txt", "r") as afile:
            adata = afile.read()
            print(adata)
    else:
        print(" \n File was moved/missing... \n ")
        
    time.sleep(5)
        




"""
# Like man, --help commands in Linux, Python has dir(), help() like commands... 

dir(str)
help(time)

"""

