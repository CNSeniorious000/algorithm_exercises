from matplotlib import pyplot as plt
from math import factorial
import numpy as np
import pickle

x, y_0, y_1, y_2, y_3 = pickle.load(open("out.pkl", "rb"))

# plt.plot(x, [y_0[i] / factorial(x) for i, x in enumerate(x)])
# plt.plot(x, [y_1[i] / factorial(x) for i, x in enumerate(x)])
# plt.plot(x, [y_2[i] / factorial(x) for i, x in enumerate(x)])
# plt.plot(x, [y_3[i] / factorial(x) for i, x in enumerate(x)])
# plt.show()
#
# plt.plot(x, [y_0[i] / x for i, x in enumerate(x)])
# plt.plot(x, [y_1[i] / x for i, x in enumerate(x)])
# plt.plot(x, [y_2[i] / x for i, x in enumerate(x)])
# plt.plot(x, [y_3[i] / x for i, x in enumerate(x)])
# plt.show()


plt.plot(np.log(x), np.log(y_0))
plt.plot(np.log(x), np.log(y_1))
plt.plot(np.log(x), np.log(y_2))
plt.plot(np.log(x), np.log(y_3))
plt.show()
