def filter_(function, sequence):
    lst = []
    for num in sequence:
        if function(num):
            list.append(num)
    return lst
