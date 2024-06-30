import random 
import matplotlib.pyplot as plt
import time 

def quickSort(A, low, high):
    if(low < high):
        p = partitionH(A, low, high)
        quickSort(A, low, p - 1)
        quickSort(A, p + 1, high)
    
    return A

def partitionL(A, low, high):
    pivot = A[low]
    start = low + 1
    end = high
    
    while(start <= end):
        
        while(start <= end and A[start] <= pivot):
            start += 1
        
        while(start <= end and A[end] > pivot):
            end -= 1
        
        if(start <= end):
            A[start], A[end] = A[end], A[start]
    
    A[low], A[end] = A[end], A[low]
    
    return end

def partitionH(A, low, high):
    pivot = A[high]
    i = low - 1
    
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[high] = A[high], A[i + 1]
    
    return i + 1

def randomListAndTime(start, end, step):
    sizes = []
    execution_times = []
    for i in range(start, end, step):
        random_list = [random.randint(0,1000) for _ in range(i)]
        sizes.append(i)
        execution_time = measureExecutionTime(random_list)
        execution_times.append(execution_time)
    
    return sizes, execution_times

def plotPerformance(sizes, execution_time):
    plt.plot(sizes, execution_time,label="Quick Sort")
    plt.xlabel("Input Sizes")
    plt.ylabel("Execution Time (s)")
    plt.title("Input Sizes vs Execution Time")
    plt.legend()
    plt.show()
    
def measureExecutionTime(A):
    start_time = time.time()
    quickSort(A, 0, len(A) - 1)
    end_time = time.time()
    return end_time - start_time
    
if __name__ == "__main__":
    quick_times = []
    sizes, quick_times = randomListAndTime(20,300,10)
    plotPerformance(sizes=sizes, execution_time=quick_times)