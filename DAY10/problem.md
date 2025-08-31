# Day 11 - Range Product Queries of Powers

**Problem Link:**  
[LeetCode 2438 - Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers/)

---

Given a positive integer `n`, there exists a **0-indexed** array called `powers`, composed of the **minimum number of powers of 2** that sum to `n`.  

- The array is sorted in **non-decreasing order**.
- There is **only one unique way** to form the array.

You are also given a **0-indexed** 2D integer array `queries`, where `queries[i] = [leftᵢ, rightᵢ]`.  

Each query asks for the **product** of all `powers[j]` where `leftᵢ ≤ j ≤ rightᵢ`.

Since the answer may be **too large**, return each query's result **modulo** `10⁹ + 7`.

---

### Rules:

- `powers` is formed by **breaking `n` into powers of 2** with the smallest possible length.
- For each query:
  - Multiply the elements of `powers` from index `leftᵢ` to `rightᵢ`.
  - Apply modulo `10⁹ + 7`.
- There will be **at least one** query.

---

### Return:

An array `answers` where `answers[i]` is the **product result** for query `i`, modulo `10⁹ + 7`.

---

### Example 1:

**Input:**  
`n = 15, queries = [[0,1],[2,2],[0,3]]`

**Output:**  
`[2, 4, 64]`

**Explanation:**  
- For `n = 15`, `powers = [1, 2, 4, 8]`.
- Query 1: `powers[0] * powers[1] = 1 * 2 = 2`  
- Query 2: `powers[2] = 4`  
- Query 3: `1 * 2 * 4 * 8 = 64`  

Modulo `10⁹ + 7` doesn’t change results → `[2, 4, 64]`.

---

### Example 2:

**Input:**  
`n = 2, queries = [[0,0]]`

**Output:**  
`[2]`

**Explanation:**  
- For `n = 2`, `powers = [2]`.  
- Query 1: `powers[0] = 2`  
- Result after modulo → `[2]`.

---

