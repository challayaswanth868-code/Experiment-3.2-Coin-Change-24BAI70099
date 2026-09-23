class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] <= amount else -1


# Test cases
solution = Solution()

print("Test Case 1:")
print("Coins = [1, 2, 5], Amount = 11")
print("Output =", solution.coinChange([1, 2, 5], 11))

print("\nTest Case 2:")
print("Coins = [2], Amount = 3")
print("Output =", solution.coinChange([2], 3))

print("\nTest Case 3:")
print("Coins = [1], Amount = 0")
print("Output =", solution.coinChange([1], 0))

print("\nTest Case 4:")
print("Coins = [1, 3, 4], Amount = 6")
print("Output =", solution.coinChange([1, 3, 4], 6))

print("\nTest Case 5:")
print("Coins = [2, 5, 10, 1], Amount = 27")
print("Output =", solution.coinChange([2, 5, 10, 1], 27))