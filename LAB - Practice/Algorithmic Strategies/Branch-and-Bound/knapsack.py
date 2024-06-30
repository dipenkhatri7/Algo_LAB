def fractional_knapsack_greedy(profit, weight, capacity):
    n = len(profit)
    profit_per_weight = [(profit[i]/weight[i], profit[i], weight[i]) for i in range(n)]
    profit_per_weight.sort(reverse=True, key=lambda x: x[0])
    max_profit = 0
    
    for ratio, p, w in profit_per_weight:
        if capacity <=0:
            break
        
        if w <= capacity:
            max_profit += p
            capacity -= w
        else:
            max_profit += ratio * capacity
            capacity = 0
    
    return max_profit


def knapsack_dp(profit, weight, capactiy):
    n = len(profit)
    dp = [[0 for i in range(capacity + 1)] for _ in range(n+1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(profit[i-1] + dp[i-1][w- weight[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

if (__name__ == '__main__'):
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50
    print(fractional_knapsack_greedy(profit, weight, capacity))
    print(knapsack_dp(profit, weight, capacity))

