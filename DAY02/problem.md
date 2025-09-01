# Day 3 - Maximum Fruits Harvested After at Most K Steps
 
**Problem Link:**  
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

You are given an array `fruits` where `fruits[i] = [positioni, amounti]` indicates that there are `amounti` fruits at the position `positioni` on an infinite x-axis.  
The array is **sorted in ascending order** by position and all positions are **unique**.

You are also given two integers:
- `startPos`: your starting position on the x-axis
- `k`: the maximum number of steps you can take (left or right, each move = 1 step)

At each position you visit (including the starting position), you **collect all fruits available** there.

Return the **maximum total number of fruits** you can collect using at most `k` steps.

---

### Example 1:

**Input:**  
fruits = [[2,8],[6,3],[8,6]]  
startPos = 5  
k = 4  

**Output:**  
9

**Explanation:**  
- Move right to position 6 (1 step) → collect 3 fruits  
- Move right to position 8 (2 more steps) → collect 6 fruits  
Total steps used: 3  
Total fruits collected: 3 + 6 = 9

---

### Example 2:

**Input:**  
fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]  
startPos = 5  
k = 4  

**Output:**  
14

**Explanation:**  
- Collect 7 fruits at position 5 (start)  
- Move left to position 4 (1 step) → collect 1 fruit  
- Move right to 6 and 7 (1 + 1 more steps) → collect 2 + 4 = 6 fruits  
Total steps: 1 (left) + 3 (right) = 4  
Total fruits: 7 + 1 + 2 + 4 = 14

---

### Example 3:

**Input:**  
fruits = [[0,3],[6,4],[8,5]]  
startPos = 3  
k = 2  

**Output:**  
0

**Explanation:**  
You can't reach any fruit positions within 2 steps, so you collect nothing.

---
