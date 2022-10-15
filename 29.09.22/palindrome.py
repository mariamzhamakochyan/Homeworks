def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False
    
list = []
for i in range(101, 1000):
    if is_palindrome(i):
        list.append(i)
print(list)
