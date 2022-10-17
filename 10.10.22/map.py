def map_(func, iter):
    res = []
    for num in iter:
        res.append(func(num))
    return res

