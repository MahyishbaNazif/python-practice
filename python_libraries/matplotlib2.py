import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x, y, linewidth = 1, marker = '*', color = 'red')
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of Values", fontsize = 14)
plt.grid(True)
plt.show()
plt.savefig('square_plot.png')
