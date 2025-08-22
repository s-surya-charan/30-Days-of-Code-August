# Day 22 - Find the Minimum Area to Cover All Ones I

**Problem Link:** [LeetCode 3195 - Find the Minimum Area to Cover All Ones I](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/)

---

You are given a **2D binary array** `grid`.

Find a rectangle with horizontal and vertical sides and the **smallest area**, such that **all the 1's in `grid` lie inside this rectangle**.

Return the **minimum possible area** of the rectangle.

---

### Example 1:

**Input:**
`grid = [[0,1,0],[1,0,1]]`

**Output:**
`6`

**Explanation:**
The smallest rectangle has:

* Height = 2
* Width = 3
  So, area = 2 × 3 = 6.

---

### Example 2:

**Input:**
`grid = [[1,0],[0,0]]`

**Output:**
`1`

**Explanation:**
The smallest rectangle is just the single cell with `1`.
So, area = 1 × 1 = 1.

---
