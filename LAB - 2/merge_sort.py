import math

def merge_sort(A, low, high):
    if low < high:
        # Calculate the middle index to divide the list into two halves
        mid = math.floor((low + high) / 2)
        
        # Recursively sort the first half
        merge_sort(A, low, mid)
        
        # Recursively sort the second half
        merge_sort(A, mid + 1, high)
        
        # Merge the two halves
        merge(A, low, mid, high)
    
    return A

def merge(A, low, mid, high):
    p = low
    q = mid + 1
    B = []  # Temporary list to store the merged result

    # Merge elements from both subarrays in sorted order
    while p <= mid and q <= high:
        if A[p] <= A[q]:
            B.append(A[p])
            p += 1
        else:
            B.append(A[q])
            q += 1

    # If there are remaining elements in the first subarray, add them to B
    while p <= mid:
        B.append(A[p])
        p += 1
    
    # If there are remaining elements in the second subarray, add them to B
    while q <= high:
        B.append(A[q])
        q += 1

    # Copy the merged elements back into the original array A
    for i in range(low, high + 1):
        A[i] = B[i - low]

if __name__ == "__main__":
    import utils  # Assumed to be a custom module for timing and plotting
    
    # List to store the times taken by merge sort for different input sizes
    merge_sort_times = []
    
    # Generate random lists of sizes and time the merge sort on them
    sizes, merge_sort_times = utils.randomListAndTime(merge_sort, 0, 1000, 10)
    
    # Plot the performance of merge sort
    utils.plotPerformance(sizes, merge_sort_times, "Merge Sort")
