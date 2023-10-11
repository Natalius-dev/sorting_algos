import matplotlib.pyplot as plt
import numpy as np
import random

plt.rcParams['toolbar'] = 'None'

input = random.sample(range(1, 101), 100)
print(input)

unsorted_arr = input.copy()

# make data:
x = np.arange(len(unsorted_arr))
sorted_arr = input.copy()

curr_min = float('inf')

plt.ion()
fig, ax = plt.subplots()
fig.suptitle("Selection Sort")
fig.canvas.manager.set_window_title("Selection Sort")
rects = ax.bar(x, sorted_arr, width=1, edgecolor="white", linewidth=0.5)

while len(unsorted_arr) > 0:
    for rect in rects:
        rect.set_color('#3e78cf')
    curr_min = min(unsorted_arr)
    rects[sorted_arr.index(curr_min)].set_color('#cf3e3e')
    sorted_arr.remove(min(unsorted_arr))
    unsorted_arr.remove(min(unsorted_arr))
    sorted_arr.insert(len(sorted_arr), curr_min)
    for rect,h in zip(rects,sorted_arr):
        rect.set_height(h)
    fig.canvas.draw()
    plt.pause(0.001)

plt.show(block=True)