import random 
import time
import matplotlib.pyplot as plt

def bubbleSort(A):
    for i in range(len(A) - 1):
        flag = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                flag = True
        if not flag:
            break
    
    return A

def randomListAndTime(start, end, step):
    sizes = []
    execution_times = []

    for i in range(start, end + 1, step):
        random_list = [random.randint(0,1000) for _ in range(i)]
        sizes.append(i)
        execution_time = measureExecutionTime(random_list)
        execution_times.append(execution_time)
    
    return sizes, execution_times

def measureExecutionTime(A):
    start_time = time.time()
    bubbleSort(A)
    end_time = time.time()
    return end_time - start_time

def plotPerformance(sizes, times):
    
    plt.plot(sizes, times, label='Bubble Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Input Size vs Execution Time')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    bubble_sort_times = []
    sizes, bubble_sort_times = randomListAndTime(20, 300, 10)
    plotPerformance(sizes, bubble_sort_times)
