#iterative()
def iterative(n):
    total = 0
    for i in range(n):
        total += 2 ** i
    return total
n = 5
print(iterative(n))    
