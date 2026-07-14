#recursive()
def recursive(n): 
    if n == 1:
        return 1
    return 2 **(n-1) + recursive(n-1)
n = 5
print(recursive(n))