def power(x, n): return x*power(x,n-1) if n>2 else x*x

print(power(5,2))