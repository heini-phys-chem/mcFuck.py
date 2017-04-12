import sys
import random

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

colors = [bcolors.HEADER, bcolors.BLUE, bcolors.GREEN, bcolors.RED, bcolors.FAIL, bcolors.ENDC]

NumOfFucksGiven = raw_input("How many Fucks do you want to give today? ")
NumOfFucksParalell = raw_input("And how many of them in paralell? ")

max = int(float(NumOfFucksGiven) / float(NumOfFucksParalell))
rest = int(NumOfFucksGiven) % int(NumOfFucksParalell)

for i in range(0, int(max)):
    print random.choice(colors) + "Fuck! " * int(NumOfFucksParalell) + str(i) + bcolors.ENDC

if (rest == 0):
    print "Congratulations, Number of Fucks given today = " + NumOfFucksGiven 
else:
    print "Fuck! " * rest
    print "Congratulations, Number of Fucks given today = " + NumOfFucksGiven 


