#Get data
with open("input.in") as f:
    output = [i.strip() for i in f.readlines()]

rows = len(output)
columns = len(output[0])

result = []
for x in range(1, rows-1):
    for y in range(1, columns-1):
        k = output[x][y]
        #Lists containing all the trees in each direction
        left = [output[x][y-i] for i in range(1, y+1)]
        right = [output[x][y+i] for i in range(1, columns-y)]
        up = [output[x-i][y] for i in range(1, x+1)]
        down = [output[x+i][y] for i in range(1, rows-x)]
        
        total = 1
        for n in (left, right, up, down):
            directionTotal = 0
            for i in range(len(n)):
                if n[i] < k:
                    directionTotal += 1
                elif n[i] >= k:
                    directionTotal += 1
                    break
            total *= directionTotal
        result.append(total)

print(max(result))