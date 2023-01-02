#Get data
with open("input.in") as f:
    stringInput = f.read()
    
#Sets can only have unique elements
def uniqueStrings(str):
    for i in range(len(str)):
        if i >= 14 and len(set([str[i-j] for j in range(14)])) == 14:
            return i+1
        
print(uniqueStrings(stringInput))