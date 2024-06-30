import random
import matplotlib.pyplot as plt
import time

def heapSort(A):
    buildMaxHeap(A)
    heapSize = len(A) - 1
    for i in range(heapSize, 1, -1):
        A[1], A[i] = A[i], A[1]
        heapSize -= 1
        maxHeapify(A, 1, heapSize)
    return A

def buildMaxHeap(A):
    heapSize = len(A) - 1
    for i in range(heapSize//2, 0, -1):
        maxHeapify(A, i, heapSize)
        
def maxHeapify(A, i, heapSize):
    left = 2*i
    right = 2*i + 1
    
    if left <= heapSize and A[left] > A[i]:
        largest = left
    else: largest = i
    if right <= heapSize and A[right] > A[largest]:
        largest = right
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heapSize)
        

def randomListAndTime(start, end, step):
    sizes = []
    execution_times = []
    for i in range(start, end, step):
        random_list = [random.randint(0,1000) for _ in range(i)]
        sizes.append(i)
        execution_time = measureExecutionTime(random_list)
        execution_times.append(execution_time)
    return sizes, execution_times

def measureExecutionTime(A):
    start = time.time()
    heapSort(A)
    end = time.time()
    return end - start

def plotPerformance(sizes, execution_times):
    plt.plot(sizes, execution_times, label='Heap Sort')
    plt.xlabel('Size of the list')
    plt.ylabel('Execution time')
    plt.title('Performance of Heap Sort')
    plt.legend()
    plt.show()

if __name__ == '__main__':

    sizes, execution_times = randomListAndTime(20, 300, 10)
    plotPerformance(sizes, execution_times)