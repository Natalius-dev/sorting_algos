import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['toolbar'] = 'None'

unsorted_arr = [3,5,10,8,9,2,6,1,7,4]

# make data:
x = np.arange(len(unsorted_arr))
sorted_arr = unsorted_arr

plt.bar(x, sorted_arr, width=1, edgecolor="white", linewidth=0.5)
plt.show()