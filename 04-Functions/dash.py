def f(string):
    new = ''
    for i in string:new += i + '-'
    return new[:-1]
print(f("Univesity"))