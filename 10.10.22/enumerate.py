def enumerate_(iterable, start=0):
    res = []
    start = 0
    for i in iterable:
        res.append((start, i))
        start += 1
    return res

