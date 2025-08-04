from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        hashmap = defaultdict(int)
        i = 0
        count = 0

        for j in range (n):
            hashmap[fruits[j]] += 1

            while len(hashmap) > 2:
                hashmap[fruits[i]] -= 1
                if hashmap[fruits[i]] == 0:
                    del hashmap[fruits[i]]
                i += 1
            count = max(count, j - i + 1)
        return count