import sys

NumOfFucksGiven = raw_input("How many Fucks do you want to give today? ")
NumOfFucksParalell = raw_input("And how many of them in paralell? ")

max = int(float(NumOfFucksGiven) / float(NumOfFucksParalell))
rest = int(NumOfFucksGiven) % int(NumOfFucksParalell)

for i in range(0, int(max)):
    print "Fuck! " * int(NumOfFucksParalell) + str(i)

if (rest == 0):
    print "Congratulations, Number of Fucks given today = " + NumOfFucksGiven 
else:
    print "Fuck! " * rest
    print "Congratulations, Number of Fucks given today = " + NumOfFucksGiven 


