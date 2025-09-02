# Day 26 - Maximum Area of Longest Diagonal Rectangle

**Problem Link:** [LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/) 

---

You are given a 2D 0-indexed integer array `dimensions`.

For all indices `i`, `0 <= i < dimensions.length`, `dimensions[i][0]` represents the **length** and `dimensions[i][1]` represents the **width** of the rectangle `i`.

Return the **area of the rectangle** having the **longest diagonal**.  
If there are multiple rectangles with the same longest diagonal, return the area of the rectangle having the **maximum area**.

---

### Example 1:

**Input:**  
`dimensions = [[9,3],[8,6]]`

**Output:**  
`48`

**Explanation:**  
- Rectangle 0: diagonal = √(9² + 3²) = √90 ≈ 9.487  
- Rectangle 1: diagonal = √(8² + 6²) = √100 = 10  
So rectangle 1 has a longer diagonal → area = 8 × 6 = 48.

---

### Example 2:

**Input:**  
`dimensions = [[3,4],[4,3]]`

**Output:**  
`12`

**Explanation:**  
- Both diagonals = √(3² + 4²) = √25 = 5  
- Both have same diagonal, so take max area = 12.

---

### Constraints:

* `1 <= dimensions.length <= 100`
* `dimensions[i].length == 2`
* `1 <= dimensions[i][0], dimensions[i][1] <= 100`
