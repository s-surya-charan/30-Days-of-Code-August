class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        total = 0

        for i in range(n):
            total += fruits[i][i]

        for pass_num in range(2):
            if pass_num == 1:
                for i in range(n):
                    for j in range(i + 1, n):
                        fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
                        
            prev = [-1] * n
            prev[n - 1] = fruits[0][n - 1]  
            for row in range(1, n - 1):
                curr = [-1] * n 
                for col in range(n):
                    if prev[col] == -1:
                        continue  
                    curr[col] = max(curr[col], prev[col] + fruits[row][col])
                    
                    if col > 0:
                        curr[col - 1] = max(curr[col - 1], prev[col] + fruits[row][col - 1])

                    if col < n - 1:
                        curr[col + 1] = max(curr[col + 1], prev[col] + fruits[row][col + 1])

                prev = curr

            total += prev[n - 1]

        return total
        
