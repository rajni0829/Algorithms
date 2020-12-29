# Python program for implementation of heap Sort
#Also finding Heap Sort's Time Taken & Consumption 
import os
import random
import time
import psutil
import matplotlib.pyplot as plt


def heapify(arr, n, i):
	largest = i      #Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

#Driver Code
size = []
heapTime = []
heapMem = []

arr_size = [10,100,500,1000,10000,100000,1000000]

for i in arr_size:
	arr = random.sample(range(i),i)
	n = len(arr)
	size.append(i)
	start = time.time()
	heapSort(arr)
	end = time.time()
	heapTime.append(end - start)

	process = psutil.Process(os.getpid())
	heap_mem = process.memory_info()[0] / float(2 ** 20)
	heapMem.append(process.memory_info()[0] / float(2 ** 20))

	print("Time Taken by HEAP SORT of array size       : {} is  {:.5f}".format(i,end-start))
	print("Memory Consumed in HEAP SORT of array size  : {} is  {:.5f}\n\n".format(i,heap_mem))

print("\nExecution Completed!")

# plt.yscale("log")
# plt.plot(size,heapTime,color="red",label = "Time")
# # plt.plot(size,heapMem,color ="yellow",label = "Memory")
# plt.legend()
# plt.grid(True)
# plt.show()
