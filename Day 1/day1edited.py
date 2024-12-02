from collections import Counter

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
    distance += abs(list1[index] - list2[index])
        
#part 2
count = Counter(list1)
for val in list2:  
    simscore += val * count[val]

print("Total Distance: " + str(distance)) #answer to part 1
print("Similarity Score: " + str(simscore)) #answer to part 2
