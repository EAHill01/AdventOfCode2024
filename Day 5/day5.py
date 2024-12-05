from functools import cmp_to_key

file = "day5input.txt"

def checkRulesFunc(rules):
    def checkRules(a,b): 
        if f"{b}|{a}" in rules: #if the first compared number is found before the second, correct
            return 1
        else:
            return -1
    return checkRules
        
rules = []
updates = []
sortedCount = 0
resortedCount = 0

with open(file) as file:
    for line in file:
        if "|" in line:
            rules.append(line.strip("\n").split())
        elif "," in line:
            updates.append(line.strip("\n").split(","))
            
rules = sum(rules,[])

for x in updates:          
    xSorted = sorted(x, key=cmp_to_key(checkRulesFunc(rules))) #sorts them according to the rules
    if x == xSorted:
        sortedCount += int(x[len(x)//2])
    else:
        resortedCount += int(xSorted[len(x)//2])
        
print("Sum of sorted middle pages: " + str(sortedCount)) #Answer to part 1
print("Sum of unsorted middle pages: " + str(resortedCount)) #Answer to part 2