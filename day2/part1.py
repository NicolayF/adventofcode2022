#Get data
with open("input.in") as f:
    data = [i for i in f.read().strip().split("\n")]

"""
A and X = Rock (1 point)
B and Y = Paper (2 points)
C and Z = Scissors (3 points)
win = 6 points
draw = 3 points
lose = 0 points
"""

sum = 0
for i in data:
    if i == "A X":
        sum += 4
    if i == "A Y":
        sum += 8
    if i == "A Z":
        sum += 3
    if i == "B X":
        sum += 1
    if i == "B Y":
        sum += 5
    if i == "B Z":
        sum += 9
    if i == "C X":
        sum += 7
    if i == "C Y":
        sum += 2
    if i == "C Z":
        sum += 6
    

print(sum)