class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M = 10**9 + 7
        powers = []
        
        for i in range(32):
            if (n & (1 << i)) != 0: 
                powers.append(1 << i)
        
        result = []
        for start, end in queries:
            product = 1
            for i in range(start, end + 1):
                product = (product * powers[i]) % M
            result.append(product)
        
        return result
