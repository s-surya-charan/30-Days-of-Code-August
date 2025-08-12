# Day 12 - Ways to Express an Integer as Sum of Powers

**Problem Link:**  
[LeetCode 2787 - Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/)

---

Given two positive integers `n` and `x`, you need to determine the **number of ways** to express `n` as the sum of the **x-th power of unique positive integers**.

Formally, count the number of distinct sets of integers `[n₁, n₂, ..., nₖ]` such that:
n = n₁ˣ + n₂ˣ + ... + nₖˣ

Since the answer can be **very large**, return the result **modulo** `10⁹ + 7`.

---

### Rules:

- Each integer can be used **at most once** in the sum.
- The integers in the sum must be **positive**.
- The order of numbers does **not** matter (`[1,3]` is the same as `[3,1]`).
- Apply modulo `10⁹ + 7` to the final answer.

---

### Return:

An integer representing the **number of unique ways** to represent `n` as the sum of `x`-th powers.

---

### Example 1:

**Input:**  
`n = 10, x = 2`

**Output:**  
`1`

**Explanation:**  
We can express `n` in only one way:  
- `3² + 1² = 9 + 1 = 10`  

No other combination of unique positive integers raised to power `2` adds up to `10`.

---

### Example 2:

**Input:**  
`n = 4, x = 1`

**Output:**  
`2`

**Explanation:**  
We can express `n` in two ways:  
- `4¹ = 4`  
- `3¹ + 1¹ = 3 + 1 = 4`

---


