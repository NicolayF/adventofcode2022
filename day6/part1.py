#Get data
with open("input.in") as f:
    stringInput = f.read()

#Sets can only have unique elements
def uniqueStrings(str):
    for i in range(len(str)):
        if i >= 3 and len(set([str[i], str[i-1], str[i-2], str[i-3]])) == 4:
            return i+1
        
print(uniqueStrings(stringInput))