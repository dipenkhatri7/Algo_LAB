import random
import time
import matplotlib.pyplot as plt

def selectionSort(A):
    for i in range(0, len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if(A[j] < A[min]):
                min = j
        
        if(min!=i):
            A[min], A[i] = A[i], A[min]
    
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
    selectionSort(A)
    end_time = time.time()
    return end_time - start_time


def plotPerformance(sizes, execution_times):
    plt.plot(sizes, execution_times, label="Selection Sort")
    plt.xlabel("Input sizes")
    plt.ylabel("Execution times (s)")
    plt.title("Input sizes v/s Execution times")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    selectionSort_times = []
    sizes, selectionSort_times = randomListAndTime(20,300,10)
    plotPerformance(sizes=sizes, execution_times=selectionSort_times)
    