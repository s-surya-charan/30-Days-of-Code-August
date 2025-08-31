from itertools import permutations
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6
        
        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
        
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = [nums[k] for k in range(len(nums)) if k!=i and k!=j]                               
                             
                        for op in [
                            nums[i] + nums[j],
                            nums[i] - nums[j],
                            nums[j] - nums[i],
                            nums[i] * nums[j]
                        ]:
                            if helper(next_nums + [op]):
                                return True
                        
                        if abs(nums[j]) > EPSILON:
                            if helper(next_nums + [nums[i] / nums[j]]):
                                return True
                        if abs(nums[i]) > EPSILON:
                            if helper(next_nums + [nums[j] / nums[i]]):
                                return True
            return False
        
        return helper([float(x) for x in cards])

        