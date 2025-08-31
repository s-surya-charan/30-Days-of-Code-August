# Day 24 - Longest Subarray of 1's After Deleting One Element

**Problem Link:** [LeetCode 1493 - Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

---

You are given a **binary array** `nums`.

You must **delete exactly one element** from it.

Return the size of the **longest non-empty subarray containing only `1's`** in the resulting array.
If no such subarray exists, return `0`.

---

### Example 1:

**Input:**
`nums = [1,1,0,1]`

**Output:**
`3`

**Explanation:**
After deleting the `0` at index 2, the array becomes `[1,1,1]`, which has length 3.

---

### Example 2:

**Input:**
`nums = [0,1,1,1,0,1,1,0,1]`

**Output:**
`5`

**Explanation:**
After deleting the `0` at index 4, the array becomes `[0,1,1,1,1,1,0,1]`.
The longest subarray of only `1's` is `[1,1,1,1,1]` of length 5.

---

### Example 3:

**Input:**
`nums = [1,1,1]`

**Output:**
`2`

**Explanation:**
You must delete one element, so the longest possible subarray is `[1,1]` of length 2.

---

### Constraints:

* `1 <= nums.length <= 10^5`
* `nums[i]` is either `0` or `1`
