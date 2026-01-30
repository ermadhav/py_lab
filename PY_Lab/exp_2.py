# <----------------------------------- PART A ----------------------------------->

# import math 

# # taking input form the user
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# midpoint1 = float((x1+x2)/2)
# midpoint2 = float((y1+y2)/2)

# print("Midpoint = ", (midpoint1 ,midpoint2) )

# print("Distance between the two pofloats:", distance)

# <----------------------------------- PART B ----------------------------------->

import sys
if(len(sys.argv)) != 4:
    print("addition of 3 arg using add.py <a> <b> ")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

result = num1*num2*num3
print(result)