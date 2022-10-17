def is_sorted(list):
    res = list[:]
    for i in range(0, len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    if res == list:
        return True
    else:
        return False
