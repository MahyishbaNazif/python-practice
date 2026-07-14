#Find int values from a file
total = 0
with open('myscript.txt', 'r')as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.isdigit():
                total = total + int(word)
print(total)                

