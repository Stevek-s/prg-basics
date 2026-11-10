def f(n, m):
    res = 0
    for i in range(n, m):
        if i % 3 == 0  or i % 2 == 0 and not i % 4 == 0: res += i
    return res
print(f(1,20))
