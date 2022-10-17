year = int(input("Enter the year to which you want to check. "))
year1 = year - 1600
count = year1 // 4
n = year1 // 100
count -= n
x = year1 // 400
count += x
print(count)
