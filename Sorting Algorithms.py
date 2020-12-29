import sys
# # total arguments
# n = int(sys.argv[1000])
# print("The number of elements is :", n )

import time
import random
import math
import matplotlib.pyplot as plt
var = (sys.getrecursionlimit())
sys.setrecursionlimit(10000000)

#INSERTION SORT
def insertion_sort(arr):
    # loop iterating
    for j in range(1,len(arr)):
        # updating key
        key = arr[j]
        i = j-1
        #enters the loop is larger num is on left of key
        while i > -1 and arr[i] > key:
            # swapping values if previous values is greater than current
            arr[i+1] = arr[i]
            i -= 1
            arr[i+1] = key


#BUBBLE SORT
def swap(arr, ind):
    #swapping adjacent indices of array
    arr[ind],arr[ind+1] = arr[ind+1],arr[ind]
    return arr

def bubble_Sort(arr):
    start = time.perf_counter()
    # Running loop till the length of array
    for i in range(0,len(arr)):
        for j in range(len(arr) - 1 - i):
            #shifting the greater value towards left
            if arr[j] > arr[j+1]:
                swap(arr,j)
    end = time.perf_counter()
    return end-start


def Selection_Sort(arr):
    # starting time
    start = time.perf_counter()
    for i in range(len(arr)):
        # setting min to first element index and checking the element to rest of the array
        min = i

        for j in range(i+1,len(arr)):
            # Checking if the first element is less than others...
            if arr[j] < arr[min]:
                # if yes ,assigning it to min value
                min = j

        # Final swapping in sorted order
        arr[min],arr[i] = arr[i],arr[min]                                  # why ??
    end = time.perf_counter()
    return end-start



# MERGE SORT
def Merge_sort(arr,p,r):
    start = time.perf_counter()
    if p < r:
        # taking middle value of the array
        q = math.floor((p+r)/2)

        # recursive call of array
        Merge_sort(arr,p,q)
        Merge_sort(arr,q+1,r)
        Merge(arr,p,q,r)
    end = time.perf_counter()
    return end-start

def Merge(arr,p,q,r):
    # dividing original array into 2 different subarrays
    subarr_1 = q-p+1
    subarr_2 = r-q
    left_list = [0] * subarr_1
    right_list = [0] * subarr_2

    # appending half in left subarray
    for i in range(0,subarr_1):
        left_list[i] = arr[p+i]

    # appending half in right subarray
    for j in range(0,subarr_2):
        right_list[j] += arr[q+1+j]

    # initialising variables to 0
    i,j,k = 0,0,p

    # following divide and conquer paradigm to sort array
    while i < subarr_1 and j < subarr_2:
        if left_list[i] <= right_list[j]:
            arr[k] = left_list[i]
            i += 1
        else:
            arr[k] = right_list[j]
            j += 1
        k += 1

    # if any element of 1st half is less,it goes to left part
    while i < subarr_1:
        arr[k] = left_list[i]
        i += 1
        k += 1

    # if any element of 2nd half is less,goes to right part
    while j < subarr_2:
        arr[k] = right_list[j]
        j += 1
        k += 1


# QUICK SORT
# To do Partition of array
def quicksort(x, l, r):
    start=time.time()
    i = l
    j = r
    # pivot element in the middle
    p = x[l + (r - l) // 2]

    while i <= j:
        while x[i] < p:
            i += 1
        while x[j] > p:
            j -= 1
        # swap
        if i <= j:
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
        # sort left list
    if l < j:
        quicksort(x, l, j)
    # sort right list
    if i < r:
        quicksort(x, i, r)
    end=time.time()
    return end-start

#creating list of numbers we are using as input
list_n = list(map(int, input("Enter size of array in single line separated with spaces(eg: 10 100 1000):: ").split()))
# list_n = [10,100,1000,10000,100000]                             #you can vary according to your convenience :)

#creating empty list for each sorting alg
list_insertion = []
list_bubble = []
list_merge = []
list_selection = []
list_quick = []

#iterating over the list_n to get the sorting time for each alg
for array_size in list_n:
    # Taking random numbers from random library one by one in range of list_n
    arr = random.sample(range(0,array_size), array_size)


    #assigning variable to the call of all sorting functions!
    start = time.perf_counter()
    (insertion_sort(arr))
    end = time.perf_counter()
    ins = end - start
    b = (bubble_Sort(arr))
    m = (Merge_sort(arr,0,len(arr)-1))
    s = (Selection_Sort(arr))
    q = quicksort(arr, 0, len(arr)-1)

    #appending time of sorting functions from variable of function call to plot the graph
    list_insertion.append(ins)
    list_bubble.append(b)
    list_merge.append(m)
    list_selection.append(s)
    list_quick.append(q)


    #Printing size of array with their required time for each instance
    print("Runtime of the INSERTION Sort program for n = {} is {}".format(array_size,ins))
    print("Runtime of the BUBBLE Sort program for n = {} is {}".format(array_size,b))
    print("Runtime of the MERGE Sort program for n = {} is {}".format(array_size,m))
    print("Runtime of the SELECTION Sort program for n = {} is {}".format(array_size,s))
    print("Runtime of the QUICK Sort program for n = {} is {}".format(array_size,q))
    print("\n\n")

print("Execution completed!")
#Plotting points of different sorting algorithm in one graph using their running time
plt.title("Comparing Performance of different sorting Algorithm")


# plt.yscale("log")
plt.plot(list_n,list_insertion,color="red",label="Insertion")
plt.plot(list_n,list_bubble,color="yellow",label="Bubble")
plt.plot(list_n,list_merge,color="blue",label="Merge")
plt.plot(list_n,list_selection,color="green",label="Selection")
plt.plot(list_n,list_quick,color="brown",label="Quick")
plt.legend()


#assigning label to the axes
plt.xlabel("<-----------  number of inputs  ----------->")
plt.ylabel("<------- time taken in seconds ------->")
plt.grid(True)
plt.show()



