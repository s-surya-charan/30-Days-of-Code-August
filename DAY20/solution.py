class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else: 
                    heights[j] = 0

            for j in range(n):
                min_height = heights[j]
                for k in range(j, -1, -1): 
                    if heights[k] == 0:
                        break
                    min_height = min(min_height, heights[k])
                    total += min_height

        return total

        
