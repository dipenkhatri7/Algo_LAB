import random
import time 
import matplotlib.pyplot as plt

def insertionSort(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i - 1
        while(j>=0 and A[j] > temp):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp
    return A

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
    start_time = time.time()
    insertionSort(A)
    end_time = time.time()
    return end_time - start_time


def plotPerformance(sizes, execution_times):
    
    plt.plot(sizes, execution_times, label='Insertion Sort')
    plt.xlabel('Input Sizes')
    plt.ylabel('Execution Time (s)')
    plt.title("Input Size vs Execution Times")
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    insertion_times = []
    sizes, insertion_times = randomListAndTime(20, 300, 10)
    plotPerformance(sizes=sizes, execution_times=insertion_times)
    