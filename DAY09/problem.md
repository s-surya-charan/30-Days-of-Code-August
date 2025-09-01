# Day 10 - Reordered Power of 2

**Problem Link:**  
[LeetCode 869 - Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/)

--- 

You are given an integer `n`. You may reorder the digits of `n` in any order (including the original order) such that the resulting number has **no leading zeros**.

Return **true** if and only if you can reorder the digits of `n` so that the resulting number is a **power of two**.

---

### Rules:

- You may **permute** the digits of `n` arbitrarily.
- The rearranged number **must not** have a leading zero.
- Check whether **any** permutation forms a number equal to `2^x` for some integer `x ≥ 0`.

---

### Return:

- `true` — if some valid permutation of the digits of `n` is a power of two.  
- `false` — otherwise.

---

### Example 1:

**Input:**  
`n = 1`

**Output:**  
`true`

---

### Example 2:

**Input:**  
`n = 10`

**Output:**  
`false`

---
