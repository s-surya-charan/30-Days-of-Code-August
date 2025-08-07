# Day 7 - Find the Maximum Number of Fruits Collected

**Problem Link:**  
[LeetCode 3363 - Find the Maximum Number of Fruits Collected](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/)

---

There is a game dungeon comprised of an `n x n` grid of rooms.

You are given a 2D array `fruits` of size `n x n`, where `fruits[i][j]` represents the number of fruits in the room at position `(i, j)`.

Three children will play in this dungeon. They start at three **corner rooms**:
- Child 1 starts at `(0, 0)`
- Child 2 starts at `(0, n - 1)`
- Child 3 starts at `(n - 1, 0)`

They will **each make exactly `n - 1` moves** to reach the destination room `(n - 1, n - 1)`, **collecting all fruits** in the rooms they visit.

Each child follows a specific movement rule:

- **Child 1** (from `(0, 0)`): Can move to  
  - `(i + 1, j)` → down  
  - `(i, j + 1)` → right  
  - `(i + 1, j + 1)` → diagonal down-right  

- **Child 2** (from `(0, n - 1)`): Can move to  
  - `(i + 1, j)` → down  
  - `(i + 1, j - 1)` → diagonal down-left  
  - `(i + 1, j + 1)` → diagonal down-right  

- **Child 3** (from `(n - 1, 0)`): Can move to  
  - `(i - 1, j + 1)` → diagonal up-right  
  - `(i, j + 1)` → right  
  - `(i + 1, j + 1)` → diagonal down-right  

**Rules:**
- A child collects **all fruits** in a room when entering it.
- If **multiple children** enter the same room, **only one** of them collects the fruits. The room is considered **emptied** after that.

---

### Return the **maximum total number of fruits** the children can collect together after reaching `(n - 1, n - 1)`.

---

### Example 1:

**Input:**  
`fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]`

**Output:**  
`100`

**Explanation:**

The best movement paths are:

- **Child 1 (green)**: `(0,0) → (1,1) → (2,2) → (3,3)`
- **Child 2 (red)**: `(0,3) → (1,2) → (2,3) → (3,3)`
- **Child 3 (blue)**: `(3,0) → (3,1) → (3,2) → (3,3)`

Collected fruits:
- Green: 1 + 6 + 11 + 16  
- Red: 4 + 8 + 12  
- Blue: 13 + 14 + 15  
→ Total = **100**

---

### Example 2:

**Input:**  
`fruits = [[1,1],[1,1]]`

**Output:**  
`4`

**Explanation:**

- **Child 1**: `(0,0) → (1,1)`
- **Child 2**: `(0,1) → (1,1)`
- **Child 3**: `(1,0) → (1,1)`

Fruits collected: 1 (from each starting room) + 1 (from final room) = **4**

---

