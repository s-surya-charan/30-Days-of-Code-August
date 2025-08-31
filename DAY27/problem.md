# Day 28 - Sort Matrix by Diagonals

**Problem Link:** [LeetCode 3446 - Sort Matrix by Diagonals](https://leetcode.com/problems/sort-matrix-by-diagonals/)

---

## Problem Statement

You are given an **n × n** square integer matrix `grid`. Return the matrix such that:

1. The **diagonals** in the **bottom-left triangle** (including the main diagonal) are sorted in **non-increasing order**.  
2. The **diagonals** in the **top-right triangle** are sorted in **non-decreasing order**.  

---

## Example 1

**Input:**
grid = [[1,7,3],
[9,8,2],
[4,5,6]]

makefile
Copy code

**Output:**
[[8,2,3],
[9,6,7],
[4,5,1]]

**Explanation:**

- Bottom-left diagonals (sorted non-increasing):
  - [1,8,6] → [8,6,1]  
  - [9,5] and [4] remain unchanged  

- Top-right diagonals (sorted non-decreasing):
  - [7,2] → [2,7]  
  - [3] remains unchanged  

---

## Example 2

**Input:**
grid = [[0,1],
[1,2]]


**Output:**
[[2,1],
[1,0]]


**Explanation:**
- Bottom-left diagonal [0,2] → [2,0] (non-increasing)  
- Others remain unchanged  

---

## Example 3

**Input:**
grid = [[1]]


**Output:**
[[1]]

**Explanation:**  
Single element diagonals remain unchanged.  

---

## Constraints

- `grid.length == grid[i].length == n`
- `1 <= n <= 10`
- `-10^5 <= grid[i][j] <= 10^5`