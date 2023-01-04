#Get data
# with open("input.in") as f:
#     input = f.read().strip("\n").split("\n")
#     output = []
#     k=0
#     for i in input:
#         output.append(list(i))
#         for j in range(len(i)):
#             output[k][j]=int(i[j])
#         k+=1
with open("input.in") as f:
    output = [i.strip() for i in f.readlines()]

rows = len(output)
columns = len(output[0])
outerTrees = rows * columns - (rows-2) * (columns-2)

count = 0
for x in range(1, rows-1):
    for y in range(1, columns-1):
        k = output[x][y]
        #Create a list containing all the trees in each direction
        left = [output[x][y-i] for i in range(1, y+1)]
        right = [output[x][y+i] for i in range(1, columns-y)] 
        up = [output[x-i][y] for i in range(1, x+1)]
        down = [output[x+i][y] for i in range(1, rows-x)]
        #Find if there are all smaller trees in any direction
        if max(left)< k or max(right)< k or max(down)< k or max(up)< k:
            count += 1

print(outerTrees+count)


