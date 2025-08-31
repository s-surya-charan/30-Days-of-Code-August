# Day 17 - New 21 Game  

**Problem Link:** [LeetCode 837 - New 21 Game](https://leetcode.com/problems/new-21-game/)  

---

Alice plays a game loosely based on the card game **"21"**:  

- Alice starts with **0 points**.  
- While she has **less than `k` points**, she continues drawing numbers.  
- Each draw gives a random integer from **[1, maxPts]** (inclusive), all equally likely.  
- Alice **stops drawing** once she reaches **k or more** points.  

Return the **probability** that Alice ends the game with **n or fewer points**.  

Answers within `1e-5` of the actual answer are accepted.  

---

### Rules:
- Alice draws numbers until she reaches at least **k**.  
- Each draw is uniformly random from **1 → maxPts**.  
- Alice stops immediately when her score ≥ `k`.  

---

### Return:
- The **probability** that Alice finishes with **≤ n points**.  

---

### Example 1:
**Input:**  
n = 10, k = 1, maxPts = 10  

**Output:**  
1.00000  

**Explanation:**  
Alice draws only once, ending with scores between 1–10 → always ≤ 10.  

---

### Example 2:
**Input:**  
n = 6, k = 1, maxPts = 10  

**Output:**  
0.60000  

**Explanation:**  
Alice draws once → possible scores: `1–10`.  
In 6 out of 10 cases, she ends ≤ 6 → probability = 0.6.  

---

### Example 3:
**Input:**  
n = 21, k = 17, maxPts = 10  

**Output:**  
0.73278  

---

