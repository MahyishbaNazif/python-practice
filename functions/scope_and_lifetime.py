#Scope and lifetime of a varible
glob = "hi i am globally avaiable"
def f1():
    local = "hi i an locally available"
    print(local)
    print(glob)
f1()  
print(glob) 
