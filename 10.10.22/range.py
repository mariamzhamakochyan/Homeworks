def range(start, stop, step):
    res = []
    while start < stop:
        res.append(start)
        start += step
    return res


start = int(input("Enter the strat: "))
stop = int(input("Enter th stop: "))
step = int(input("Ente the step: "))
print(range(start, stop, step))
