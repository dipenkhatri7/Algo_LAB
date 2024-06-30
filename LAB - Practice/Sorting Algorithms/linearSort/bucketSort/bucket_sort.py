import math

def bucketSort(A):
    n = len(A)
    B = [ [] for _ in range(n) ]
    for i in range(n):
        B[math.floor(n * A[i])].append(A[i])
    
    for i in range(n):
        B[i].sort()
    
    print(B)
    index = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[index] = B[i][j]
            index += 1
    
    return A


if __name__ == "__main__":
    A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print(bucketSort(A))