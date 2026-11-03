n = 1
nn = 0
for i in range(20): 
    if i % 2 == 0: 
        print(nn)
        nn += n
    else:
        print(n)
        n += nn
    