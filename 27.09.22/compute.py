def com(x, y):
    z = x - y
    if x - y < 0:
        res = -(x - y) / (x + y)
        return res
    elif x + y == 0:
        return "The numerator can't be equal to 0: "
    else:
        res = (x - y) / (x + y)
        return(res)
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(com(x, y))
