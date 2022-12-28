#Get data
#Items are stored in strings
with open("input.in") as f:
    data = [i for i in f.read().split("\n")]


#Find top3 elves and sum
sum = 0
arr = []
for i in data:
    if i == '':
        arr.append(sum)
        sum = 0
    else:
        sum += int(i)

arr.sort(reverse=True)
top3 = arr[0]+arr[1]+arr[2]
print(top3)