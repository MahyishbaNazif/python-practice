#Sum of Sums of Natural Numbers
'''Given the following series;
   1+(1+2)+(1+2+3)+(1+2+3+4)+---+(1+2+3+---+n) is a sum of sums of the first n natural numbers.'''
n = int(input())
k = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        k = k + j
print(k)        
#Time Complexity O(n^2)