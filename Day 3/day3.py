import re

file = "day3input.txt"

correctMul = re.findall(r"mul\(\d+,\d+\)", open(file).read()) #gets all correctly formatted muls

count=0
for line in correctMul:
    a,b = re.findall(r'\d+', line)
    count += int(a) * int(b)

print("All added up multiplications: " + str(count)) #Answer to part 1

doDontMul = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open(file).read()) #gets all correctly formatted muls, do's, and don't's in text

count=0
process = True
for line in doDontMul:
    if line == "do()":
        process = True
    elif line == "don't()":
        process = False
    elif process: #only process muls with the latest do
        a,b = re.findall(r'\d+', line)
        count += int(a) * int(b)
        
print("All added up multiplications with conditionals: " + str(count)) #Answer to part 2