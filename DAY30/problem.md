# Day 31 - Sudoku Solver

**Problem Link:** [LeetCode 37 - Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

---

## Problem Statement

Write a program to **solve** a Sudoku puzzle by filling the empty cells.

A valid Sudoku solution must satisfy all of the following rules:

- Each of the digits `1-9` occurs **exactly once** in each **row**.  
- Each of the digits `1-9` occurs **exactly once** in each **column**.  
- Each of the digits `1-9` occurs **exactly once** in each of the **nine 3×3 sub-boxes**.  

The `'.'` character indicates **empty cells**.

Your function should **modify the board in-place** to produce the valid solution.  
It is guaranteed that the input board has **only one** solution.

---

## Example 1

**Input:**

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]


**Output:**


[
["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]
]


**Explanation:**  
The input board is solved so that every row, column, and 3×3 box contains each digit `1–9` exactly once.

---

## Constraints

- `board.length == 9`  
- `board[i].length == 9`  
- `board[i][j]` is a digit `'1'–'9'` or `'.'`  
- The input board has **exactly one** valid solution.

---

