
from os import close
# ADVENT OF CODE DAY ONE PART ONE
# opens file to read
measure = open("input_files/input.txt", "r")
# turns file lines into list
measurements = list(measure)
# ✓- create 2 variables
# ✓ - One to hold first item in list (since this item is the first it does 
# not have a previous measurement to compare) turn into integer
# ✓ - Second variable set count to 0 and increase count only if current item is greater than previous number
# ✓ - create for loop to go through list
# ✓ - start for loop at index 1 as index 0 will be held in variable at beginning
# ✓ - turn list items into Integers
# ✓ - check if item is greater than variable One 
# ✓ - if item is greater than variable One change variable One to item and increase variable Two by 1
# ✓ - if item is not greater than variable One change variable One to item and move to next item
#  without increase variable Two
# ✓ - loop through whole list
# ✓ - print variable Two


current = int(measurements[0])
counter = 0

for measurement in measurements[1:]:
    num = int(measurement)
    if num > current:
       current = num
       counter += 1
       continue
    else:
        current = num
        continue
print(counter)

# ADVENT OF CODE DAY ONE PART TWO
# ✓ - create two variables
# ✓ - variable one used to home sum of first three measurements
# ✓ - variable two will hold the count of how many measurement sums are greater than previous
# ✓ - create a for loop
# ✓ - loop through list starting at index 1 and turn each item into integer
# ✓ - create variable called sum
# - in variable sum take current index and add next two items in list
# ✓ - create if statement
# ✓ - if sum is greater than variable one
# ✓ - replace value of variable one with sum value
# ✓ - increase variable two by one 
# ✓ - else if sum in less than variable one
# ✓ - replace value of variable one with sum value
# ✓ - do not increase variable two
# ✓ - loop through to complete list
# ✓ - when loop is finished print variable two
# ✓ - use try and except to break from loop when error occurs

total = int(measurements[0]) + int(measurements[0 + 1]) + int(measurements[0 + 2])
counterTwo = 0

for i in range(len(measurements[1:])):
    try:
        sumNums = int(measurements[i]) + int(measurements[i+1]) + int(measurements[i + 2])
        if sumNums > total:
            total = sumNums
            counterTwo += 1
            continue
        else:
            total = sumNums
            continue
    except: 
        break
print(counterTwo) 



measure.close()

