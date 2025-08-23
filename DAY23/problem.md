# Day 23 - Find the Minimum Area to Cover All Ones II

**Problem Link:** [LeetCode 3197 - Find the Minimum Area to Cover All Ones II](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/)

---

You are given a **2D binary array** `grid`.

You need to find **3 non-overlapping rectangles** with horizontal and vertical sides, each having a **non-zero area**, such that **all the 1's in `grid` lie inside these rectangles**.

Return the **minimum possible sum of the areas** of these rectangles.

> Note: The rectangles are allowed to **touch** but cannot overlap.

---

### Example 1:

**Input:**
`grid = [[1,0,1],[1,1,1]]`

**Output:**
`5`

**Explanation:**

* The 1's at `(0,0)` and `(1,0)` are covered by a rectangle of area **2**.
* The 1's at `(0,2)` and `(1,2)` are covered by a rectangle of area **2**.
* The 1 at `(1,1)` is covered by a rectangle of area **1**.

Total = 2 + 2 + 1 = **5**.

---

### Example 2:

**Input:**
`grid = [[1,0,1,0],[0,1,0,1]]`

**Output:**
`5`

**Explanation:**

* The 1's at `(0,0)` and `(0,2)` are covered by a rectangle of area **3**.
* The 1 at `(1,1)` is covered by a rectangle of area **1**.
* The 1 at `(1,3)` is covered by a rectangle of area **1**.

Total = 3 + 1 + 1 = **5**.

---
