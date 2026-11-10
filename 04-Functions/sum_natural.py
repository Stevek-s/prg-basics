def sun_natural(n):
    return n+sun_natural(n-1) if n > 2 else n+1

print(sun_natural(9))