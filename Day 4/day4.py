file = "day4input.txt"

#global variable used
foundXmas = 0

def findX(wordsearch):
    for i in range(0, len(wordsearch)):
        for j in range(0, len(wordsearch[i])):
            if wordsearch[i][j] == "X":
                checkWord(wordsearch, "X", i, j, [0,0], len(wordsearch), len(wordsearch[i]))
               
def checkWord(wordsearch, letter, i, j, dir, vertLen, horLen):
    global foundXmas
    directions=[[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
    match letter:
        case "X":
            goal = "M" #check every direction from X to find an M
            for x in directions: #checks every direction from the X
                check = checkDir(wordsearch, (i + x[0]), (j + x[1]), goal, vertLen, horLen)
                if check:
                    print("Found " + goal + ", searching for next letter")
                    checkWord(wordsearch, goal, (i + x[0]), (j + x[1]), x, vertLen, horLen)
        case "M":
            goal = "A" #only check the same direction that M was found in
            check = checkDir(wordsearch, (i + dir[0]), (j + dir[1]), goal, vertLen, horLen)
            if check:
                print("Found " + goal + ", searching for next letter")
                checkWord(wordsearch, goal, (i + dir[0]), (j + dir[1]), dir, vertLen, horLen)
        case "A": 
            goal = "S" #only check the same direction that A was found in
            check = checkDir(wordsearch, (i + dir[0]), (j + dir[1]), goal, vertLen, horLen)
            if check:
                foundXmas += 1 #adds to the global variable
                print("Found S, adding to FoundXmas")
    
def checkDir(wordsearch, i,j, goal, vertLen, horLen):
    if i != vertLen and j != horLen and i>=0 and j>=0: #not at the edge of the puzzle
        if wordsearch[i][j] == goal:
            return True
        else:
            return False
    else:
        return False
        
wordsearch = []
with open(file) as file:
    for line in file:
        wordsearch.append(list(str(line.split())))
 
findX(wordsearch)
print("Number of XMAS words found: " + str(foundXmas))