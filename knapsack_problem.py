def knapsack(W, weight, value, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(
                    value[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

weight = [1, 3, 4, 5]
value = [1, 4, 5, 7]
W = 7
n = len(weight)

print("Maximum value =", knapsack(W, weight, value, n))
