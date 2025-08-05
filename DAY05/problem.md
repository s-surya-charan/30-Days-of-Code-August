# Day 5 - Fruits Into Baskets II

**Problem Link:**  
https://leetcode.com/problems/fruits-into-baskets-ii/

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where:

- `fruits[i]` represents the quantity of the `iᵗʰ` type of fruit
- `baskets[j]` represents the capacity of the `jᵗʰ` basket

From **left to right**, place the fruits into baskets according to the following rules:

- Each fruit type must be placed in the **leftmost available** basket with a **capacity greater than or equal to** the quantity of that fruit type.
- Each basket can hold **only one type of fruit**.
- If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

Return the **number of fruit types** that remain unplaced after all possible allocations are made.

---

### Example 1:

**Input:**  
fruits = [4, 2, 5]  
baskets = [3, 5, 4]  

**Output:**  
1

**Explanation:**  
- fruits[0] = 4 → placed in baskets[1] = 5  
- fruits[1] = 2 → placed in baskets[0] = 3  
- fruits[2] = 5 → cannot be placed in baskets[2] = 4  
→ One fruit type is unplaced.

---

### Example 2:

**Input:**  
fruits = [3, 6, 1]  
baskets = [6, 4, 7]  

**Output:**  
0

**Explanation:**  
- fruits[0] = 3 → placed in baskets[0] = 6  
- fruits[1] = 6 → cannot go in baskets[1] = 4, but fits in baskets[2] = 7  
- fruits[2] = 1 → placed in baskets[1] = 4  
→ All fruits are placed successfully.

---