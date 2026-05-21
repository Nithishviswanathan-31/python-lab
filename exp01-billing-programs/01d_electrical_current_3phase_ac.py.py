#program for calculating electric current

import math
print("Calculating electric current of 3 phase AC circuit:\n")
volts=int(input("Enter the volts value:"))
amperes=int(input("Enter the amperes value:"))
power=math.sqrt(3)*volts*amperes
print("Power=%fKVA"%power)