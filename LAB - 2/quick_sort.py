import utils

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort the elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1

if __name__ == "__main__":
    # List to store the times taken by quick sort for different input sizes
    quick_sort_times = []
    
    # Generate random lists of sizes and time the quick sort on them
    sizes, quick_sort_times = utils.randomListAndTime(quick_sort, 0, 1000, 10)
    
    # Plot the performance of quick sort
    utils.plotPerformance(sizes, quick_sort_times, "Quick Sort")
