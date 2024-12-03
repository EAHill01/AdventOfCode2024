''' Rules:
- All levels in a row either increase or decrease
- No levels can be the same
- Increases and decreases must be between 1 and 3
'''

def probCheck(row):
    status = 0 #1 means level is increasing, -1 means level is decreasing, 0 outside of index=0 means broken
    for index, val in enumerate(row):
        if index == 0:
            if row[index] > row[index+1]: #decreasing
                status = -1
            elif row[index] < row[index+1]: #increasing
                status = 1
            else: #equal
                status = 0
                
        if (index != len(row)-1) and (status != 0): #not the last value and still okay
            if (status == -1) and not(val-1>=row[index+1]>=val-3): #if decreasing and not 1 to 3 less than former
                status = 0
            elif (status == 1) and not(val+1<=row[index+1]<=val+3): #if increasing and not 1 to 3 more than former
                status = 0   
                   
        if (status==0):
            return False
        
        if (index == len(row)-1): #last value
            return True
    

file = "day2input.txt"
levels = []

with open(file) as file:
    for line in file:
        levels.append([int(x) for x in line.split()])

safe = 0
probSafe = 0
for row in levels:
    status = 0 #1 means level is increasing, -1 means level is decreasing, 0 outside of index=0 means broken
    for index, val in enumerate(row):
        if index == 0:
            if row[index] > row[index+1]: #decreasing
                status = -1
            elif row[index] < row[index+1]: #increasing
                status = 1
            else: #equal
                status = 0
                row2 = [i for i in row]
                row2.pop(index)
                check = probCheck(row2)
                if check == True:
                    probSafe += 1
                elif check == False:
                    row2 = [i for i in row]
                    row2.pop(index+1)
                    check = probCheck(row2)
                    if check == True:
                        probSafe += 1
                    else:
                        print(row)
                
        if (index != len(row)-1) and (status != 0): #not the last value and still okay
            if (status == -1) and not(val-1>=row[index+1]>=val-3): #if decreasing and not 1 to 3 less than former
                status = 0
                row2 = [i for i in row]
                row2.pop(index)
                check = probCheck(row2)
                if check == True:
                    probSafe += 1
                elif check == False:
                    row2 = [i for i in row]
                    row2.pop(index+1)
                    check = probCheck(row2)
                    if check == True:
                        probSafe += 1
                    elif check == False and index == 1: #only check index 0 if index is 1, and dec/inc is switched
                        row2 = [i for i in row]
                        row2.pop(index-1)
                        check = probCheck(row2)
                        if check == True:
                            probSafe += 1
                        else:
                            print(row)
            elif (status == 1) and not(val+1<=row[index+1]<=val+3): #if increasing and not 1 to 3 more than former
                status = 0   
                row2 = [i for i in row]
                row2.pop(index)
                check = probCheck(row2)
                if check == True:
                    probSafe += 1
                elif check == False:
                    row2 = [i for i in row]
                    row2.pop(index+1)
                    check = probCheck(row2)
                    if check == True:
                        probSafe += 1
                    elif check == False and index == 1: #only check index 0 if index is 1, and dec/inc is switched
                        row2 = [i for i in row]
                        row2.pop(index-1)
                        check = probCheck(row2)
                        if check == True:
                            probSafe += 1
                        else:
                            print(row)
                   
        if (status==0):
            break
        
        if (index == len(row)-1): #last value
            safe += 1
    
print("Number of Safe Rows: " + str(safe)) #Answer to first part
print("Number of Safe Rows with Dampener: " + str(safe + probSafe))