class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        windowSum = 1.0 
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts

            if i < k:
                windowSum += dp[i] 
            else:
                res += dp[i]
            left = i - maxPts
            
            if 0 <= left < k:
                windowSum -= dp[left]

        return res
