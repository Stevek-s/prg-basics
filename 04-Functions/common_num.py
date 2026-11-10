def f(num):
    char = ''
    times = 0
    times_fin = 0
    for i in num:
        for y in num:
            if i==y: times += 1
        if times > times_fin:
            times_fin = times
            char = i
        times = 0
    return char

print(f("5233165554211"))


