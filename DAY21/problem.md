# Day 21 - Count Submatrices With All Ones

**Problem Link:** [LeetCode 1504 - Count Submatrices With All Ones](https://leetcode.com/problems/count-submatrices-with-all-ones/)

---

You are given an `m x n` **binary matrix** `mat`.
Return the **number of submatrices that have all ones**.

A submatrix is a rectangular part of the matrix that is contiguous in both rows and columns.

---

### Example 1:

**Input:**
`mat = [[1,0,1],[1,1,0],[1,1,0]]`

**Output:**
`13`

**Explanation:**

* Rectangles of size 1x1: 6
* Rectangles of size 1x2: 2
* Rectangles of size 2x1: 3
* Rectangles of size 2x2: 1
* Rectangles of size 3x1: 1

Total = 13.

---

### Example 2:

**Input:**
`mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]`

**Output:**
`24`

**Explanation:**

* Rectangles of size 1x1: 8
* Rectangles of size 1x2: 5
* Rectangles of size 1x3: 2
* Rectangles of size 2x1: 4
* Rectangles of size 2x2: 2
* Rectangles of size 3x1: 2
* Rectangles of size 3x2: 1

Total = 24.

---


