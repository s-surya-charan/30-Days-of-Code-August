# Day 27 - Length of Longest V-Shaped Diagonal Segment

## Problem Statement

You are given a 2D integer matrix `grid` of size `n x m`, where each element is either `0`, `1`, or `2`.

A **V-shaped diagonal segment** is defined as:

* The segment **starts with 1**.
* The subsequent elements follow this infinite sequence: `2, 0, 2, 0, ....`
* The segment:

  * Starts along a diagonal direction (**↘, ↙, ↖, or ↗**).
  * Continues the sequence in the same diagonal direction.
  * Makes at most **one clockwise 90-degree turn** to another diagonal direction while maintaining the sequence.

Return the **length of the longest V-shaped diagonal segment**. If no valid segment exists, return `0`.

---

## Examples

**Example 1:**

```
Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
Output: 5
```

Explanation: The longest V-shaped diagonal segment has a length of 5:

```
(0,2) → (1,3) → (2,4), turn, (3,3) → (4,2)
```

---

**Example 2:**

```
Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
Output: 4
```

Explanation: The longest segment is:

```
(2,3) → (3,2), turn, (2,1) → (1,0)
```

---

**Example 3:**

```
Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
Output: 5
```

Explanation: The longest segment is a straight diagonal:

```
(0,0) → (1,1) → (2,2) → (3,3) → (4,4)
```

---

**Example 4:**

```
Input: grid = [[1]]
Output: 1
```

Explanation: Only one element `(0,0)` forms the segment.

---

## Constraints

* `n == grid.length`
* `m == grid[i].length`
* `1 <= n, m <= 500`
* `grid[i][j]` is either `0`, `1`, or `2`.

---

that returns the **length of the longest V-shaped diagonal segment**.

