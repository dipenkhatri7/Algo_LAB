def knapsack_01_brute_force(profit, weight, capacity):
    def knapsack_recursive(index, remaining_capacity):
        if index == len(profit) or remaining_capacity == 0:
            return 0
        
        if weight[index] > remaining_capacity:
            return knapsack_recursive(index + 1, remaining_capacity)
        
        include = profit[index] + knapsack_recursive(index + 1, remaining_capacity - weight[index])
        exclude = knapsack_recursive(index + 1, remaining_capacity)
        
        return max(include, exclude)
    
    return knapsack_recursive(0, capacity)


def fractional_knapsack_brute_force(profit, weight, capacity):
    n = len(profit)
    max_profit = 0

    def generate_combinations(start, total_weight, total_profit):
        nonlocal max_profit
        if total_weight <= capacity:
            max_profit = max(max_profit, total_profit)
        
        if start >= n or total_weight > capacity:
            return
        
        for i in range(start, n):
            if total_weight + weight[i] <= capacity:
                generate_combinations(i + 1, total_weight + weight[i], total_profit + profit[i])
            else:
                fraction = (capacity - total_weight) / weight[i]
                max_profit = max(max_profit, total_profit + profit[i] * fraction)

    generate_combinations(0, 0, 0)

    return max_profit


def fractional_knapsack_greedy(profit, weight, capacity):
    n = len(profit)
    profit_per_weight = [(profit[i] / weight[i], profit[i], weight[i]) for i in range(n)]
    profit_per_weight.sort(reverse=True, key=lambda x: x[0])
    
    max_profit = 0
    current_capacity = capacity

    for ratio, p, w in profit_per_weight:
        if current_capacity <= 0:
            break
        if w <= current_capacity:
            max_profit += p
            current_capacity -= w
        else:
            max_profit += ratio * current_capacity
            current_capacity = 0

    return max_profit


def dp_knapsack(profit, weight, capacity):
    n = len(profit)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i-1] <= w:
                dp[i][w] = max(profit[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]


def recursive_knapsack(profit, weight, capacity, n):
    if (n == 0 or capacity == 0):
        return 0
    if(weight[n-1] > capacity):
        return recursive_knapsack(profit, weight, capacity, n-1)
    else:
        return max(recursive_knapsack(profit, weight, capacity, n-1), profit[n-1] + recursive_knapsack(profit, weight, capacity - weight[n-1], n-1))
    
    

if (__name__ == '__main__'):
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50

    print(knapsack_01_brute_force(profit, weight, capacity))
    print(fractional_knapsack_brute_force(profit, weight, capacity))
    print(fractional_knapsack_greedy(profit, weight, capacity))
    print(dp_knapsack(profit, weight, capacity))
    print(recursive_knapsack(profit, weight, capacity, len(profit)))