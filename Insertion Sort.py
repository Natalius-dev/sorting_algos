# unsorted_arr decreases as time goes on
# sorted_arr starts as unsorted_arr
# sorted_arr must keep the same length as time goes on

import matplotlib.pyplot as plt
import numpy as np
import random

plt.rcParams['toolbar'] = 'None'

input = random.sample(range(1, 101), 100)
print(input)

latest_checked = 0
current_checked = 0

unsorted_arr = input.copy()

# make data:
x = np.arange(len(unsorted_arr))
sorted_arr = input.copy()

plt.ion()
fig, ax = plt.subplots()
fig.suptitle("Insertion Sort")
fig.canvas.manager.set_window_title("Insertion Sort")
rects = ax.bar(x, sorted_arr, width=1, edgecolor="white", linewidth=0.5)

while latest_checked <= 100:
    for rect in rects:
        rect.set_color('#3e78cf')
    rects[current_checked+1].set_color('#cf3e3e')
    
    for index in range(latest_checked):
        current_checked = index
        j = index-1
        while j >= 0 and current_checked < sorted_arr[j]:
            sorted_arr[j+1] = sorted_arr[j]
            j -= 1
        sorted_arr[j+1] = current_checked

    latest_checked += 1

    for rect,h in zip(rects,sorted_arr):
        rect.set_height(h)
    fig.canvas.draw()
    plt.pause(0.001)

plt.show(block=True)