# Day X - Maximum 69 Number  

**Problem Link:** [LeetCode 1323 - Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/)  

---
  
You are given a positive integer **num** consisting only of digits **6** and **9**.  

Return the **maximum number** you can get by changing **at most one digit**:  
- `6 → 9`  
- `9 → 6`  

---

### Rules:
- You can change **at most one digit**.  
- Changing is optional (if the number is already maximum).  
- The number only contains digits `6` and `9`.  

---

### Return:
- The **maximum possible integer** after changing at most one digit.  

---

### Example 1:
**Input:**  
num = 9669  

**Output:**  
9969  

**Explanation:**  
- Changing the first digit results in 6669.  
- Changing the second digit results in 9969.  
- Changing the third digit results in 9699.  
- Changing the fourth digit results in 9666.  
The maximum number is **9969**.  

---

### Example 2:
**Input:**  
num = 9996  

**Output:**  
9999  

**Explanation:**  
Changing the last digit 6 → 9 gives the maximum number.  

---

### Example 3:
**Input:**  
num = 9999  

**Output:**  
9999  

**Explanation:**  
No change is needed since the number is already maximum.  

---
