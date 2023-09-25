import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, bitrate=1800)

def gen_random_numbers_in_range(low, high, n):
    return random.sample(range(low, high), n)

plt.rcParams['toolbar'] = 'None'

input = gen_random_numbers_in_range(1, 101, 100)
print(input)

unsorted_arr = input.copy()

# make data:
x = np.arange(len(unsorted_arr))
sorted_arr = input.copy()

curr_min = float('inf')

plt.ion()
fig, ax = plt.subplots()
rects = ax.bar(x, sorted_arr, width=1, edgecolor="white", linewidth=0.5)

ims = []

while len(unsorted_arr) > 0:
    ims.append(rects)
    curr_min = min(unsorted_arr)
    sorted_arr.remove(min(unsorted_arr))
    unsorted_arr.remove(min(unsorted_arr))
    sorted_arr.insert(0, curr_min)
    for rect,h in zip(rects,sorted_arr):
        rect.set_height(h)
    fig.canvas.draw()
    plt.pause(0.001)

im_ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
im_ani.save('im.mp4', writer=writer)
plt.show(block=True)