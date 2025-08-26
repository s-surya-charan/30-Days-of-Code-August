import math 

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxx = -1.0
        res = 0

        for l, b in dimensions:
            d = math.sqrt(l * l + b * b)

            if d > maxx:
                maxx = d
                res = l * b
            elif d == maxx:
                res = max(res, l * b)
        return res
