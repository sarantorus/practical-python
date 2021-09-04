#sears.py

bill_thickness = 0.11*0.001 #bill thickness in meters
sears_height = 442 #Height (meters)
day = 1
num_bills=1

while num_bills*bill_thickness < sears_height:
    print(day,num_bills, num_bills*bill_thickness)
    day = day+1
    num_bills = num_bills*2
print('No. of Days',day)
print('No. of bills',num_bills)
print('Final height', num_bills*bill_thickness)

#Python While Loop is used to execute a block of statements repeatedly until a
#given condition is satisfied.
#And when the condition becomes false,
#the line immediately after the loop in the program is executed.
#While loop falls under the category of indefinite iteration

