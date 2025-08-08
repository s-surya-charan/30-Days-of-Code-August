class Solution:
    def soupServings(self, n: int) -> float:
        # If n is very large, the probability approaches 1
        if n > 4500:
            return 1.0
        
        self.memo = {}
        return self.solve(n, n)

    def solve(self, x: int, y: int) -> float:
        # Both soups run out together
        if x <= 0 and y <= 0:
            return 0.5
        
        # Soup A runs out first
        if x <= 0:
            return 1.0
        
        # Soup B runs out first
        if y <= 0:
            return 0.0
        
        # Memoization key
        key = (x, y)
        if key in self.memo:
            return self.memo[key]
        
        # Each of the 4 serving options has probability 0.25
        ans = (
            self.solve(x - 100, y) +
            self.solve(x - 75, y - 25) +
            self.solve(x - 50, y - 50) +
            self.solve(x - 25, y - 75)
        ) * 0.25
        
        self.memo[key] = ans
        return ans