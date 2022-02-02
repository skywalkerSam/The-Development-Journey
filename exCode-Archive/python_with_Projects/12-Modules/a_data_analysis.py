
import time
import os
import pandas


while (True):
    if (os.path.exists("12-Modules/a_data.csv")):
        with open("12-Modules/a_data.csv") as a_file:
            a_data = pandas.read_csv("12-Modules/a_data.csv")
            a_mean = a_data.mean()
            print(a_data)
            print(a_mean)
    else:
        print(" \n The file was moved/missing... \n ")

    time.sleep(10)
