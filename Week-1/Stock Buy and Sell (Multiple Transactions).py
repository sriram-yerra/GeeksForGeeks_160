def max_profit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    profit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

if __name__ == "__main__":
    prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))
    print("Maximum Profit:", max_profit(prices))
    