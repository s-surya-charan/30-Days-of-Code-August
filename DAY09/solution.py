class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        def reorder(x):
            return ''.join(sorted(str(x)))

        powers_check = {reorder(1 << i) for i in range (31)}
        return reorder(n) in powers_check
         
