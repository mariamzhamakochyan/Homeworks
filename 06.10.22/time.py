time = int(input("Enter hour: "))
if time > 12 or time < 1:
    print("Time must be between 1 and 12")
else:
    am_pm = int(input("am(1) or pm(2)? "))
    hours = int(input("How many hours ahead? "))
    res = time + hours
    if time + hours > 12:
        res = res -12
    if am_pm == 1:
        print(f"New hour: {res} am")
    else:
        print(f"New hour: {res} pm")
        
