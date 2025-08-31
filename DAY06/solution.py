class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        total = 0

        # Step 1: Diagonal contribution (child 1 from top-left to bottom-right)
        for i in range(n):
            total += fruits[i][i]

        # Step 2: Handle child 2 (top-right to bottom-right) and child bottom-left to bottom-right)
        for pass_num in range(2):
            # For second pass (child 3), transpose the grid to reuse logic
            if pass_num == 1:
                for i in range(n):
                    for j in range(i + 1, n):
                        fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

            # Initialize DP arrays: prev holds max fruits till previous row
            prev = [-1] * n
            prev[n - 1] = fruits[0][n - 1]  # Starting position for child 2 or transposed child 3

            # Iterate through rows 1 to n-2 (excluding destination cell)
            for row in range(1, n - 1):
                curr = [-1] * n  # Temp array to store current row's DP values
                for col in range(n):
                    if prev[col] == -1:
                        continue  # Skip invalid paths

                    # Move straight down
                    curr[col] = max(curr[col], prev[col] + fruits[row][col])

                    # Move left
                    if col > 0:
                        curr[col - 1] = max(curr[col - 1], prev[col] + fruits[row][col - 1])

                    # Move right
                    if col < n - 1:
                        curr[col + 1] = max(curr[col + 1], prev[col] + fruits[row][col + 1])

                # Swap for next iteration
                prev = curr

            # Add the max fruits collected upon reaching (n-1, n-1)
            total += prev[n - 1]

        return total
        