# Day 18 - 24 Game  

**Problem Link:** [LeetCode 679 - 24 Game](https://leetcode.com/problems/24-game/)  

---
 
You are given an integer array `cards` of length **4**.  
Each card contains a number in the range **[1, 9]**.  

You should arrange the numbers on these cards in a **mathematical expression** using the operators  
`['+', '-', '*', '/']` and parentheses `(` and `)` to get the value **24**.  

---

### Rules & Restrictions:
- Division `'/'` represents **real division**, not integer division.  
  - Example: `4 / (1 - 2 / 3) = 4 / (1/3) = 12`.  
- Every operation is **between two numbers**.  
  - Unary operations like `-1 - 1 - 1 - 1` are **not allowed**.  
- Numbers cannot be concatenated.  
  - Example: `[1,2,1,2] → "12 + 12"` is **invalid**.  

Return **true** if you can form an expression that evaluates to **24**, otherwise **false**.  

---

### Example 1:
**Input:**  
`cards = [4,1,8,7]`  

**Output:**  
`true`  

**Explanation:**  
`(8 - 4) * (7 - 1) = 24`  

---

### Example 2:
**Input:**  
`cards = [1,2,1,2]`  

**Output:**  
`false`  

---
