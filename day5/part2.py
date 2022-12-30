with open("input.in") as f:
    crateString, instructions = (i.splitlines() for i in f.read().strip("\n").split("\n\n"))

inputStacks = [crate.replace("    ","[0]").replace(" ","").replace("[","") for crate in crateString[:-1]]
inputStacks = [crate.split("]")[:-1] for crate in inputStacks]
stacksTotal = int(crateString[-1].replace(" ","")[-1])

#Initial stacks
stacks = [[] for i in range(stacksTotal)]
for i in range(len(inputStacks)):
    for j in range(stacksTotal):
        if inputStacks[i][j] != '0':
            stacks[j].insert(0, inputStacks[i][j])

#Clean instructions string into:
#number of crates to move, from what pile to move and where.
for instruction in instructions:
    instruction = instruction.replace("move ","").replace("from ","").replace("to ","").strip().split(" ")
    instruction = [int(i) for i in instruction]
    numberOfCrates = instruction[0]
    fromPile = instruction[1]
    toPile = instruction[2]
    for i in range(numberOfCrates, 0, -1):
        stacks[toPile-1].append(stacks[fromPile-1][-i])
        del stacks[fromPile-1][-i]

def showStacks():
    print("Stacks:\n")
    for i in range(len(stacks)):
        print(i, stacks[i])
    print("\n")

showStacks()
