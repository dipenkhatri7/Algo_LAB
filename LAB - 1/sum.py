def sum(A):
    sum = 0
    for i in A:
        sum += i
    return sum

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    print(sum(A))