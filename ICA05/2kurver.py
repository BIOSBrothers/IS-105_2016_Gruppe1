import matplotlib.pyplot as plt
#Setter metadata på grafen
plt.title("Test resultater")
plt.xlabel("Test nummer")
plt.ylabel("sekunder")
plt.legend("test resultater")
plt.legend('y = test1’,’y = test2’, ‘y = test3’ ,’Location','southwest')

linje1, = plt.plot([0,1,2], [1.43332910538,2.07897149205,4.03414204929], label="10 in l", linestyle="--")
linje2, = plt.plot([0,1,2], [3.24785399437,4.74935065522,6.83749383712], label="search_fast", linewidth=3)
linje3, = plt.plot([0,1,2], [3.59211611748,5.07962299208,9.84938238271], label="search_slow", linewidth=3)
first_legend = plt.legend(handles=[linje2], loc=1)
ax = plt.gca().add_artist(first_legend)
plt.legend(handles=[linje3], loc=4)
plt.axis([0, 2, 0, 20])
plt.show()