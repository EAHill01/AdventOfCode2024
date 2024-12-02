file = "day1input.txt"

list1 = []
list2 = []

with open(file) as file:
    for line in file:
        row = line.split()
        list1.append(int(row[0]))
        list2.append(int(row[1]))

list1.sort()
list2.sort()

distance = 0 #var for part 1
simscore = 0 #var for part 2

for index, val in enumerate(list1):
    #part 1
    if list1[index] > list2[index]: #if list1 is bigger
        distance += list1[index] - list2[index]
    else: #if list2 is bigger or they are the same
        distance += list2[index] - list1[index]
        
    #part 2
    occ = 0
    for x in list2:
        if x == val:
            occ += 1
    simscore += occ * val

print("Total Distance: " + str(distance)) #answer to part 1
print("Similarity Score: " + str(simscore)) #answer to part 2


    

