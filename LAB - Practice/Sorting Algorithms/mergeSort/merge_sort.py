import math
import random
import time
import matplotlib.pyplot as plt

def mergeSort(A, low, high):
    if(low < high):
        mid = math.floor((low + high) / 2)
        mergeSort(A, low, mid)
        mergeSort(A, mid + 1, high)
        merge(A, low, mid, high)
    
    return A

def merge(A, low, mid, high):
    p = low
    q = mid + 1
    B = []
    
    while(p <= mid and q <= high):
        if(A[p] < A[q]):
            B.append(A[p])
            p += 1
        else:
            B.append(A[q])
            q += 1
    
    if(p > mid):
        while(q <= high):
            B.append(A[q])
            q += 1
    
    if(q > high):
        while(p <= mid):
            B.append(A[p])
            p += 1
  
    for i in range(low, high + 1):
        A[i] = B[i-low]


def randomListAndTime(start, end, step):
    sizes = []
    execution_times = []
    for i in range(start, end, step):
        random_list = [random.randint(0,1000) for _ in range(i)]
        sizes.append(i)
        execution_time = measureExecutionTime(random_list, 0, len(random_list) - 1)
        execution_times.append(execution_time)
    
    return sizes, execution_times

def measureExecutionTime(A, low, high):
    start_time = time.time()
    mergeSort(A,low,high)
    end_time = time.time()
    return end_time - start_time
    

def plotPerformance(sizes, execution_time):
    plt.plot(sizes, execution_time, label='Merge Sort')
    plt.xlabel("Input sizes")
    plt.ylabel("Execution times (s)")
    plt.title("Input sizes vs Execution time")
    plt.legend()
    plt.show()
    
if __name__ == "__main__":

    merge_sort_times = []
    sizes, merge_sort_times = randomListAndTime(20, 400, 10)
    plotPerformance(sizes=sizes, execution_time=merge_sort_times)