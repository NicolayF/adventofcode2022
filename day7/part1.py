#Get data
with open("input.in") as f:
    data = [i for i in f.read().strip().split("\n")]

data = [i.replace("$ ","") for i in data]

#Path queue
path = []
#Memory Size
sizes = {}

for command in data:
    words = command.split()
    if words[0] == "cd":
        if words[1] == "..":
            path.pop()
        else:
            path.append(words[1])
            sizes["_".join(path)] = 0
    elif words[0] == "ls" or words[0] == "dir":
        continue
    else:
        size = int(words[0])
        for i in range(len(path)+1):
            if '_'.join(path[:i]) != "":
                sizes['_'.join(path[:i])] += size

#TODO: '_'.join(path[:i]) is adding an extra space.
print(sizes)
result = 0
for i in sizes:
    if sizes[i] <= 100000:
        result += sizes[i]

print(result)

#ERROR: /foo/bar/foo or /foo/foo/foo
#this are different foo's