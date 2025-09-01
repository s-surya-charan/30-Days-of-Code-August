class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4500:
            return 1.0
        
        self.memo = {}
        return self.solve(n, n)

    def solve(self, x: int, y: int) -> float:
        if x <= 0 and y <= 0:
            return 0.5
        
        if x <= 0:
            return 1.0

        if y <= 0:
            return 0.0
        
        key = (x, y)
        if key in self.memo:
            return self.memo[key]
        
        ans = (
            self.solve(x - 100, y) +
            self.solve(x - 75, y - 25) +
            self.solve(x - 50, y - 50) +
            self.solve(x - 25, y - 75)
        ) * 0.25
        
        self.memo[key] = ans
        return ans
