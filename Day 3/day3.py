import re

file = "day3input.txt"

input = open(file, "r")

correctMul = re.findall(r"mul\(\d+,\d+\)", input.read()) #gets all correctly formatted muls

count = 0
for line in correctMul:
    numbers = list(map(int, re.findall(r'\d+', line))) #gets only the integers from each line
    count += numbers[0] * numbers[1]

print("All added up multiplications: " + str(count)) #Answer to part 1

doDontMul = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open(file).read()) #gets all correctly formatted muls, do's, and don't's in text

count=0
process = True
for line in doDontMul:
    if line == "do()":
        process = True
    elif line == "don't()":
        process = False
    elif process == True: #only process muls with the latest do
        numbers = list(map(int, re.findall(r'\d+', line))) #gets only the integers from each line
        count += numbers[0] * numbers[1]
        
print("All added up multiplications with conditionals: " + str(count)) #Answer to part 2