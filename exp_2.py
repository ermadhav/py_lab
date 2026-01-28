# <----------------------------------- PART A ------------------------------------>

import math # importing the math for sqrt func

# taking input form the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#finding the sqrt and putting in the dinstance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#finding the midpofloat of the both the pofloats
midpoint1 = float((x1+x2)/2)
midpoint2 = float((y1+y2)/2)

#printing the midpoint
print("Midpoint = ", (midpoint1 ,midpoint2) )

#printing the midpoint
print("Distance between the two pofloats:", distance)
