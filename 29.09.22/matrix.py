n = 5
matrix = [[int(input("Enter a number: ")) for i in range(n)] for j in range(n)]
print(matrix)
dict_ = {}
key = dict_.keys()
for i in matrix:
    for j in i:
        if j in key:
            dict_[j] += 1
        else:
            dict_.update({j:1})
print(dict_)
res = []
x = list(dict_.values())
x.sort()
x = x[-3:]
for i in x:
    for j in dict_.keys():
        if dict_[j] == i:
            print(j)
