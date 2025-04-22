class Solution:
    def maximumProfit(self, prices):
        # code here
        prof = 0
        min_price = prices[0]
        for price in prices[1:]:
            min_price = min(min_price, price)
            prof = max(prof, price - min_price)
            
        return prof
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends