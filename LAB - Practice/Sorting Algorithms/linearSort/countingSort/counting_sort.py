def countingSort(A, n, k):
    
    count = [0] * (k+1)
    
    for i in range(n):
        count[A[i]] += 1
    
    for i in range(1, k +1):
        count[i] += count[i-1]
    
    B = [0] * n
    
    for i in range(n-1, -1, -1):
        B[count[A[i]]-1] = A[i] 
        count[A[i]] -= 1
    
    for i in range(n):
        A[i] = B[i]
        
    return A


if __name__=="__main__":
    A= [0,2,4,5,1,2,0,2,1,2,3,2,4,5,2,2,1,2,0,5,1,0,0]
    k = max(A)
    print(countingSort(A,len(A), k))
