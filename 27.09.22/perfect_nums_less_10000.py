def is_perfect(num):
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    return False

list = []
for i in range(2, 10000):
    if is_perfect(i):
        list.append(i)
print(list)
