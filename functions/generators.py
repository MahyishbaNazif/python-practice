def creator1():
    i = 1
    while i <= 200:
        yield i
        i += 1
print(creator1())
x = creator1()
print(next(x)) 
print(list(x)) 