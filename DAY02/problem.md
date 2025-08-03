# Day 2 - Rearranging Fruits

**Problem Link:**  
https://leetcode.com/problems/rearranging-fruits/description/

You have two fruit baskets containing `n` fruits each. You are given two 0-indexed integer arrays `basket1` and `basket2` representing the cost of fruits in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

- Choose two indices `i` and `j`, and swap the `i`th fruit of `basket1` with the `j`th fruit of `basket2`.
- The **cost of the swap** is `min(basket1[i], basket2[j])`.

Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same.

Return the **minimum cost** to make both the baskets equal, or `-1` if impossible.

---

### Example 1:

**Input:**  
basket1 = [4, 2, 2, 2]  
basket2 = [1, 4, 1, 2]  

**Output:**  
1

**Explanation:**  
Swap basket1[1] = 2 with basket2[0] = 1 (cost = 1)  
Now basket1 = [4, 1, 2, 2] and basket2 = [2, 4, 1, 2]  
After sorting both:  
basket1 = [1, 2, 2, 4]  
basket2 = [1, 2, 2, 4] → Equal

---

### Example 2:

**Input:**  
basket1 = [2, 3, 4, 1]  
basket2 = [3, 2, 5, 1]  

**Output:**  
-1

**Explanation:**  
No sequence of swaps can make the two baskets equal.

---

