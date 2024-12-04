file = "day4input.txt"

foundXmas = 0

def findA(wordsearch):
    for i in range(0, len(wordsearch)):
        for j in range(0, len(wordsearch[i])):
            if wordsearch[i][j] == "A":
                checkWord(wordsearch, i, j, len(wordsearch), len(wordsearch[i]))
                
def checkWord(wordsearch, i, j, vertLen, horLen):
    global foundXmas
    if i < vertLen-1 and j < horLen-1 and i>0 and j>0: #not at the edge of the puzzle
        if wordsearch[i-1][j-1] == "M" and wordsearch[i-1][j+1] == "M" and wordsearch[i+1][j+1] == "S" and wordsearch[i+1][j-1] == "S":
            foundXmas+=1
        elif wordsearch[i-1][j-1] == "S" and wordsearch[i-1][j+1] == "M" and wordsearch[i+1][j+1] == "M" and wordsearch[i+1][j-1] == "S":
            foundXmas+=1
        elif wordsearch[i-1][j-1] == "S" and wordsearch[i-1][j+1] == "S" and wordsearch[i+1][j+1] == "M" and wordsearch[i+1][j-1] == "M":
            foundXmas+=1
        elif wordsearch[i-1][j-1] == "M" and wordsearch[i-1][j+1] == "S" and wordsearch[i+1][j+1] == "S" and wordsearch[i+1][j-1] == "M":
            foundXmas+=1
    
wordsearch = []
with open(file) as file:
    for line in file:
        wordsearch.append(list(str(line.split())))
 
findA(wordsearch)
print("Number of X-MAS words found: " + str(foundXmas)) #Answer to part 2