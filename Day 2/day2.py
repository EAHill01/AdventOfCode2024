''' Rules:
- All levels in a row either increase or decrease
- No levels can be the same
- Increases and decreases must be between 1 and 3
'''

file = "day2input.txt"
levels = []

with open(file) as file:
    for line in file:
        levels.append([int(x) for x in line.split()])

safe = 0
for row in levels:
    status = 0 #1 means level is increasing, -1 means level is decreasing, 0 outside of index=0 means broken
    #print("")
    #print(row)
    for index, val in enumerate(row):
        if index == 0:
            if row[index] > row[index+1]: #decreasing
                #print("decreasing")
                status = -1
            elif row[index] < row[index+1]: #increasing
                #print("increasing")
                status = 1
            else: #equal
                #print("equal")
                status = 0
                
        if (index != len(row)-1) and (status != 0): #not the last value and still okay
            #print(str(row[index]) + " " + str(row[index+1]))
            if (status == -1) and not(val-1>=row[index+1]>=val-3): #if decreasing and not 1 to 3 less than former
                #print("decreasing broken")
                status = 0
            elif (status == 1) and not(val+1<=row[index+1]<=val+3): #if increasing and not 1 to 3 more than former
                #print("increasing broken")
                status = 0
            #else:
                #print("working for now, difference = " + abs(val - row[index+1]))
        elif (status==0):
            #print("break")
            break
        elif (index == len(row)-1): #last value
            #print("safe")
            safe += 1
    

print("Number of Safe Rows: " + str(safe)) #Answer to first part
            
            
                
            