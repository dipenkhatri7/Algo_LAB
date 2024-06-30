
def countingSort(A, n, exp):
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = A[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        index = A[i] // exp
        output[count[index % 10] - 1] = A[i]
        count[index % 10] -= 1
        
    for i in range(n):
        A[i] = output[i]
        
    return A

def radixSort(A):
    max_num = max(A)
    exp = 1
    while max_num // exp > 0:
        countingSort(A, len(A), exp)
        exp *= 10
    return A

if __name__ == "__main__":
    A = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", A)
    sorted_A = radixSort(A)
    print("Sorted array:", sorted_A)