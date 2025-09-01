from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        mp = Counter()
        minEl = float('inf')
        
        for x in basket1:
            mp[x] += 1
            minEl = min(minEl, x)
        
        for x in basket2:
            mp[x] -= 1
            minEl = min(minEl, x)
        
        final_list = []
        
        for cost, count in mp.items():
            if count == 0:
                continue
            
            if count % 2 != 0:
                return -1  # Impossible to make both baskets equal
            
            # Add half of the surplus/deficit to final list
            for _ in range(abs(count) // 2):
                final_list.append(cost)
        
        final_list.sort()
        result = 0
        
        # We only need to process the smaller half
        for i in range(len(final_list) // 2):
            result += min(final_list[i], 2 * minEl)
        
        return result

