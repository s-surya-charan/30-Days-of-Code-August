# Day 4 - Fruit Into Baskets  

**Problem Link:**  
https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `iᵗʰ` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules:

- You only have **two baskets**, and each basket can only hold **one type** of fruit.
- There is **no limit** on the amount of fruit each basket can hold.
- You can start at **any tree** and must pick exactly one fruit from every tree (including the start tree) while moving **to the right**.
- The picked fruits must **fit in one of your baskets**.
- Once you reach a tree with a fruit type that doesn't fit in your baskets, you must **stop**.

Return the **maximum number of fruits** you can pick.

---

### Example 1:

**Input:**  
fruits = [1, 2, 1]  

**Output:**  
3

**Explanation:**  
We can pick from all 3 trees → [1, 2, 1]

---

### Example 2:

**Input:**  
fruits = [0, 1, 2, 2]  

**Output:**  
3

**Explanation:**  
We can pick from trees [1, 2, 2].  
If we started at the first tree, we could only pick from [0, 1].

---

### Example 3:

**Input:**  
fruits = [1, 2, 3, 2, 2]  

**Output:**  
4

**Explanation:**  
We can pick from trees [2, 3, 2, 2].  
If we started at the beginning, we could only collect from [1, 2].

---

