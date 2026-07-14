#Find the remainder without using % operator
'''Write a program to find the reaminder when a positive number X is divided with a positive number Y. 
  You are allowed to use only + & - symbols. Use of /, // or % is prohibited.'''
def fun(x, y):
    if x < y:
        return x
    return fun(x - y, y)
print (fun(30, 10))