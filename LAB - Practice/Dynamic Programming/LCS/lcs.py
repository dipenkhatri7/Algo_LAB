def recursion_LCS(X,Y,m,n):
    if m == len(X) or n == len(Y):
        return 0
    elif X[m] == Y[n]:
        return 1 + recursion_LCS(X,Y, m+ 1, n+1)
    else:
        return max(recursion_LCS(X,Y,m+1,n), recursion_LCS(X,Y,m,n+1))
    
    
def memoization_LCS(X,Y,m,n):
    dp = [[-1 for i in range (len(X)+1)] for _ in range(len(Y)+1)]
    if m == len(X) or n == len(Y):
        return 0
    if (dp[m][n] != -1):
        return dp[m][n]
    elif X[m] == Y[n]:
        dp[m][n] = 1 + memoization_LCS(X, Y, m + 1, n + 1)
        return dp[m][n]
    else:
        dp[m][n] = max(memoization_LCS(X,Y,m+1,n), memoization_LCS(X,Y,m,n+1))
        return dp[m][n]


def tabulation_LCS(X,Y):
    dp = [[0 for i in range(len(X)+1)] for _ in range(len(Y)+1)]
    
    for i in range(1,len(Y)+1):
        for j in range(1,len(X)+1):
            if X[j-1] == Y[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i][j-1], dp[i-1][j])
    return dp[len(Y)][len(X)]

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(recursion_LCS(X,Y,0,0))
    
    X = "AAGGBBBTAB"
    Y = "AGXTXAAFYB"
    print(memoization_LCS(X,Y,0,0))
    
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(tabulation_LCS(X,Y))

    
    
    
