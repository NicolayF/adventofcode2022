import string

#lowercase + uppercase list
alphabet = list(string.ascii_letters)

#print(alphabet)
#print(alphabet.index('a') + 1)


#Get data
with open("input.in") as f:
    data = [i for i in f.read().strip().split("\n")]

#print(data)
#for goes by 3 elements at times
#compares the 3 strings with set()
#find the letter in the alphabet
#sum the index to the total
sum = 0
for i in range(0,len(data),3):
    str1, str2, str3 = data[i], data[i+1], data[i+2]
    commonLetter = list(set(str1) & set(str2) & set(str3))
    sum += alphabet.index(commonLetter[0]) + 1

print(sum)