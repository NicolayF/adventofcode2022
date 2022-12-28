import string

#lowercase + uppercase list
alphabet = list(string.ascii_letters)

#print(alphabet)
#print(alphabet.index('a') + 1)


#Get data
with open("input.in") as f:
    data = [i for i in f.read().strip().split("\n")]

#print(data)
sum = 0
for i in data:
    str1, str2 = i[:len(i)//2], i[len(i)//2:]
    commonLetter = list(set(str1) & set(str2))
    sum += alphabet.index(commonLetter[0]) + 1

print(sum)