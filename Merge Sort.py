import matplotlib.pyplot as plt
import numpy as np
import random
import array

plt.rcParams['toolbar'] = 'None'

input = random.sample(range(1, 101), 100)
print(input)

unsorted_arr = input.copy()

# make data:
x = np.arange(len(unsorted_arr))
sorted_arr = input.copy()

plt.ion()
fig, ax = plt.subplots()
fig.suptitle("Merge Sort")
fig.canvas.manager.set_window_title("Merge Sort")
rects = ax.bar(x, sorted_arr, width=1, edgecolor="white", linewidth=0.5)

smallest_arr_len = len(sorted_arr)

def mergeSort(arr):
    if len(arr) > 1:
        #print(arr)

        arr_mid = len(arr)//2

        arr_L = arr[:arr_mid]
        arr_R = arr[arr_mid:]

        for rect in rects:
            rect.set_color('#3e78cf')
        rects[sorted_arr.index(arr_R[0])].set_color('#cf3e3e')
        plt.pause(0.001)
        
        mergeSort(arr_L)
        mergeSort(arr_R)

        i = j = k = 0
    
        # Copy data to temp arrays arr_L[] and arr_R[]
        while i < len(arr_L) and j < len(arr_R):
            if arr_L[i] <= arr_R[j]:
                arr[k] = arr_L[i]
                i += 1
            else:
                arr[k] = arr_R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(arr_L):
            arr[k] = arr_L[i]
            i += 1
            k += 1

        while j < len(arr_R):
            arr[k] = arr_R[j]
            j += 1
            k += 1

mergeSort(sorted_arr)
for rect,h in zip(rects,np.array(sorted_arr).flatten()):
    rect.set_height(h)
fig.canvas.draw()
plt.pause(0.001)
plt.show(block=True)