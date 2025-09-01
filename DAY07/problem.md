# Day 8 - Soup Servings

**Problem Link:**  
[LeetCode 808 - Soup Servings](https://leetcode.com/problems/soup-servings/)
 
---

You have **two soups**, `A` and `B`, each starting with `n` mL. On each turn, one of the following four serving operations is chosen **at random**, each with probability **0.25**:

1. Pour **100 mL** from **A** and **0 mL** from **B**  
2. Pour **75 mL** from **A** and **25 mL** from **B**  
3. Pour **50 mL** from **A** and **50 mL** from **B**  
4. Pour **25 mL** from **A** and **75 mL** from **B**

---

### Rules:

- If the operation requires more soup than remains in either type, you pour **all that remains**.
- The amounts are poured **simultaneously** during that turn.
- The process stops **when either soup runs out**.
- If **both run out in the same turn**, it's considered a **tie**.

---

### Return:

The **probability** that **soup A runs out first**, **plus** **half** the probability that **both run out simultaneously**.

*Answers within `10^-5` of the true value are accepted.*

---

### Example 1:

**Input:**  
`n = 50`

**Output:**  
`0.62500`

**Explanation:**  
- Operations 1 & 2 → A runs out first → probability 1  
- Operation 3 → both run out → probability 0.5  
- Operation 4 → B runs out first → probability 0  

Result = 0.25 × (1 + 1 + 0.5 + 0) = **0.625**

---

### Example 2:

**Input:**  
`n = 100`

**Output:**  
`0.71875`

---
