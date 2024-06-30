import utils # Importing utility functions for generating random lists and plotting performance

def selectionSort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

if __name__ == "__main__":
    selection_times = []
    # Generate random lists and measure execution time for selection sort
    sizes, selection_times = utils.randomListAndTime(selectionSort, 20, 300, 10) 
    # Plot the performance
    utils.plotPerformance(sizes, selection_times, 'Selection Sort')
