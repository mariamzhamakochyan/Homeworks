def fib(n):
    cache = [0] * (n + 1)
    if n < 0:
        return (f"You can not enter a negative number!")
    elif n <= 1:
       return n
    if cache[n] != 0:
       return cache[n]
    else:
       cache[n] = fib(n -1) +  fib(n -2)
       return cache[n]
n = int(input("Enter a number:"))
print(fib(n))
