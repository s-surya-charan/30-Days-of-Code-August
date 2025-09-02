# Day 29 - Alice and Bob Playing Flower Game
  
**Problem Link:** [LeetCode 3021 - Alice and Bob Playing Flower Game](https://leetcode.com/problems/alice-and-bob-playing-flower-game/)

---

## Problem Statement

Alice and Bob are playing a turn-based game on a field with **two lanes of flowers** between them.  

- There are `x` flowers in the first lane.  
- There are `y` flowers in the second lane.  

The game proceeds as follows:

1. Alice takes the **first turn**.  
2. In each turn, a player must **choose one of the lanes** and pick **one flower** from that lane.  
3. If after a turn, **there are no flowers left at all**, the current player **captures their opponent** and **wins the game**.  

You are given two integers `n` and `m`.  

- The number of flowers `x` in the first lane must be in the range `[1, n]`.  
- The number of flowers `y` in the second lane must be in the range `[1, m]`.  

Return the number of possible pairs `(x, y)` such that **Alice wins the game**.

---

## Example 1

**Input:**
`n = 3, m = 2`

**Output:**
`3`

**Explanation:**
- The following pairs satisfy the conditions:
- (1, 2)
- (3, 2)
- (2, 1)

---

## Example 2
**Input:**

`n = 1, m = 1`

**Output:**

`0`

**Explanation:**

- No pairs satisfy the conditions described in the statement.
---

