import utils # Importing utility functions for generating random lists and plotting performance

def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A
    
if __name__ == "__main__":
    insertion_times = []
    # Generate random lists and measure execution time for insertion sort
    sizes, insertion_times = utils.randomListAndTime(insertionSort, 20, 300, 10) 
    # Plot the performance
    utils.plotPerformance(sizes, insertion_times, 'Insertion Sort')
    