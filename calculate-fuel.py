import requests
import math

def calulateFuel(moduleWeight):
    return (math.floor((moduleWeight / 3)) - 2)

def run():
    with open("C:\\Users\\Harry\\Documents\\weights.txt") as inputFile:
        content = inputFile.readlines()
        content = [x.strip() for x in content]
        totalFuelRequired = 0

        for input in content:
            totalFuelRequired += calulateFuel(int(input))
            print(totalFuelRequired)
        
run()
