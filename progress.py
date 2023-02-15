import matplotlib.pyplot as plt
import numpy as np

progress = []
for i in range(10, 50,5):
    p = [np.random.randint(i//2,i), i]
    progress.append(p)
progress = np.array(progress)
print(progress[:,1])
x = progress[:,1]
y = progress[:,0]
r = np.divide(y,x)*100.
# x = np.linspace(-1, 1, 50)
# y1 = 2*x + 1
# y2 = 2**x + 1

plt.figure()
plt.plot(x, y) 
plt.plot(x, r)  


plt.xlabel("Number of words")
plt.ylabel("Number of correct words")
plt.title("flash card progress chart")

plt.show()