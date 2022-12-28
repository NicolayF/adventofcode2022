#Get data
#Items are stored in strings
with open("input.in") as f:
    data = [i for i in f.read().split("\n")]


#Find max calories
max = -1
sum = 0
for i in data:
    if i == '':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += int(i)

print(max)