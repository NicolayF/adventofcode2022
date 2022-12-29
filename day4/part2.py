#spli multiple delimiters
import re

#Get data
with open("input.in") as f:
    data = [i for i in f.read().strip().split("\n")]

sum = 0
for i in data:
    arr = re.split(r'-|,', i)
    elf1Start = int(arr[0])
    elf1End = int(arr[1])
    elf2Start = int(arr[2])
    elf2End = int(arr[3])
    if ((elf1End >= elf2Start) & (elf2End >= elf1Start)) \
        | ((elf2End >= elf1Start) & (elf1End >= elf2Start)):
        sum += 1

print(sum)
