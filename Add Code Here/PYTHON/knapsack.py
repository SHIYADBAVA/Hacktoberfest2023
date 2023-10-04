def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruct the solution
    selected_items = []
    w, i = capacity, n
    while w > 0 and i > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    # Return the maximum value and the selected items
    return dp[n][capacity], selected_items[::-1]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
