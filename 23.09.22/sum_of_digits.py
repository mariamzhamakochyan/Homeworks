#1
def sum(num):
    sum_ = 0
    for digit in str(num):
        sum_ += int(digit) 
    return sum_
num = int(input("Enter a numer: "))
print(sum(num))

#2
def sum(num):
    sum_ = 0
    while num != 0:
        res = num % 10
        num = num // 10
        sum_ += res
    return sum_
num = int(input("Enter a numer: "))
print(sum(num))
