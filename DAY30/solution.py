from typing import List

class DLXNode:
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None
        self.row_id = None
        self.node_id = None


class ColumnNode(DLXNode):
    def __init__(self, name):
        super().__init__()
        self.size = 0
        self.name = name


class DLX:
    def __init__(self, cols):
        self.header = ColumnNode("header")
        self.columns = []
        self.solution = []
        prev = self.header
        for name in cols:
            col = ColumnNode(name)
            self.columns.append(col)
            col.right = prev.right
            col.left = prev
            prev.right.left = col
            prev.right = col
            col.up = col.down = col
            prev = col

    def add_row(self, row_id, nodes):
        first = None
        for col in nodes:
            column = self.columns[col]
            new_node = DLXNode()
            new_node.column = column
            new_node.row_id = row_id
            if first is None:
                first = new_node
            new_node.left = first.left
            new_node.right = first
            first.left.right = new_node
            first.left = new_node
            new_node.up = column.up
            new_node.down = column
            column.up.down = new_node
            column.up = new_node
            column.size += 1

    def cover(self, col):
        col.right.left = col.left
        col.left.right = col.right
        i = col.down
        while i != col:
            j = i.right
            while j != i:
                j.down.up = j.up
                j.up.down = j.down
                j.column.size -= 1
                j = j.right
            i = i.down

    def uncover(self, col):
        i = col.up
        while i != col:
            j = i.left
            while j != i:
                j.column.size += 1
                j.down.up = j
                j.up.down = j
                j = j.left
            i = i.up
        col.right.left = col
        col.left.right = col

    def search(self, k=0):
        if self.header.right == self.header:
            return True
        c = self.header.right
        mn = float("inf")
        col = None
        while c != self.header:
            if c.size < mn:
                mn = c.size
                col = c
            c = c.right
        self.cover(col)
        r = col.down
        while r != col:
            self.solution.append(r.row_id)
            j = r.right
            while j != r:
                self.cover(j.column)
                j = j.right
            if self.search(k + 1):
                return True
            j = r.left
            while j != r:
                self.uncover(j.column)
                j = j.left
            self.solution.pop()
            r = r.down
        self.uncover(col)
        return False


class Solution:
    def solveSudoku(self, board):
        def sudoku_exact_cover():
            cols = []
            for r in range(9):
                for c in range(9):
                    cols.append(f"cell {r}{c}")
            for r in range(9):
                for d in range(1, 10):
                    cols.append(f"row {r}{d}")
            for c in range(9):
                for d in range(1, 10):
                    cols.append(f"col {c}{d}")
            for b in range(9):
                for d in range(1, 10):
                    cols.append(f"box {b}{d}")
            return cols

        cols = sudoku_exact_cover()
        dlx = DLX(cols)
        for r in range(9):
            for c in range(9):
                for d in range(1, 10):
                    b = (r // 3) * 3 + c // 3
                    row_id = (r, c, d)
                    nodes = [
                        r * 9 + c,
                        81 + r * 9 + (d - 1),
                        162 + c * 9 + (d - 1),
                        243 + b * 9 + (d - 1),
                    ]
                    dlx.add_row(row_id, nodes)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    d = int(board[r][c])
                    b = (r // 3) * 3 + c // 3
                    row_id = (r, c, d)
                    nodes = [
                        r * 9 + c,
                        81 + r * 9 + (d - 1),
                        162 + c * 9 + (d - 1),
                        243 + b * 9 + (d - 1),
                    ]
                    dlx.solution.append(row_id)
                    for col in nodes:
                        dlx.cover(dlx.columns[col])

        dlx.search()
        for (r, c, d) in dlx.solution:
            board[r][c] = str(d)
