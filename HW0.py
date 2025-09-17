import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.sin(2*x), label="sin(2x)")
plt.title("Sine Waves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()