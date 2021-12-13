# - open and read file
# - create two variables one called horizontal and second called depth
# - both variables will have a starting value at 0
# - will need to create a loop 
# - create a list of each line 
# - loop through list 
# - create if/elif/else statements to check list[0]
# - turn list[1] into integer
# - if key is equal to 'forward' add list[1] to variable horizontal
# - if key is not equal to 'forward' check to see if key is equal to 'down'
# - if key is equal to 'down' add list[1] to variable depth
# - if key is not equal to 'down' check to see if key is equal to 'up'
# - if key is equal to 'up' subtract list[1] to variable depth
# - continue until loop comes to the end
# - at the end print out horizontal variable multiplied by depth variable
# - close file can use with at the beginning to automatically close file without calling close() function
# - realized dictionary will not work as it will just change values

with open("input_files/dive.txt", "r") as d:
    lines = d.readlines()
d_list = list(lines)

# DAY TWO PART ONE
horizontal = 0
depth = 0
for items in d_list:
    x = items.split(" ")
    if x[0] == 'forward':
        horizontal += int(x[1])
        continue
    elif x[0] == 'down':
        depth += int(x[1])
        continue
    elif x[0] == 'up':
        depth -= int(x[1])
        continue
    
# print(horizontal * depth)

# DAY TWO PART TWO
# - create 3 variables
# - one variable for horizontal
# - one variable for depth
# - one variable for aim
# - create a for loop to loop through list
# - create a list with split with item I am currently looping through
# - check to see if item[0] is 'down'
# - if item[0] is 'down' increase the aim variable by item[1]
# - else check to see if item[0] is 'up'
# - if item[0] is 'up' decrease the aim variable by item[1]
# - else check if item[0] is 'forward'
# - if item[0] is 'forward' increase variable horizontal by item[1]and
# increase depth by aim multiplied by item[1]
# - at the end of the loop multiple horizontal by depth

horizontalTwo = 0
depthTwo = 0
aim = 0
for items in d_list:
    x = items.split(" ")
    if x[0] == 'forward':
        horizontalTwo += int(x[1])
        aimSum = aim * int(x[1])
        depthTwo += aimSum
        continue
    elif x[0] == 'down':
        aim += int(x[1])
        continue
    elif x[0] == 'up':
        aim -= int(x[1])
        continue

print(horizontalTwo * depthTwo)