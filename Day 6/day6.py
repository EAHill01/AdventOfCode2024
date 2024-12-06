file = "day6input.txt"

floormap = []
direction = 0 #degrees, starting north, clockwise

def checkGuard(rowIndex, colIndex, direction, floormap):
    cont = True
    while cont:
        match direction:
            case 0:
                if rowIndex == 0:
                    cont=False
                elif floormap[rowIndex-1][colIndex] == "#": #change direction
                    direction = 90
            case 90:
                if colIndex == len(floormap[rowIndex])-1:
                    cont=False
                    print(cont)
                elif floormap[rowIndex][colIndex+1] == "#":
                    direction = 180
            case 180:
                if rowIndex == len(floormap)-1:
                    cont=False
                elif floormap[rowIndex+1][colIndex] == "#":
                    direction = 270
            case 270:
                if colIndex == 0:
                    cont=False
                elif floormap[rowIndex][colIndex-1] == "#":
                    direction = 0
        rowIndex, colIndex = moveGuard(rowIndex,colIndex,direction,floormap,cont)
                
def moveGuard(rowIndex, colIndex, direction, floormap, cont):
    floormap[rowIndex][colIndex] = "X"
    if cont: #doing whilst cont = false is index error
        match direction:
            case 0:
                floormap[rowIndex-1][colIndex] = "^"
                return rowIndex-1,colIndex
            case 90:
                floormap[rowIndex][colIndex+1] = "^"
                return rowIndex,colIndex+1
            case 180:
                floormap[rowIndex+1][colIndex] = "^"
                return rowIndex+1,colIndex
            case 270:
                floormap[rowIndex][colIndex-1] = "^"
                return rowIndex,colIndex-1
    return rowIndex,colIndex
            
with open(file) as file:
    for line in file:
        floormap.append(list(line.strip("\n")))

for index, val in enumerate(floormap): #find starting arrow
    if "^" in val:
        x,y = index, val.index("^")
        
checkGuard(x,y,direction, floormap)

xCount = 0
for i in range(len(floormap)):
    for j in range(len(floormap[i])):
        if floormap[i][j] == "X":
            xCount += 1
            
print("Number of positions visited: " + xCount) #Answer for Part 1
            



        