class Solution:
    def hammingWeight(self, n: int) -> int:
        #SOL 1(NOT BAD)
        res = 0
        while n:
            res += n % 2 
            n = n >> 1
        return res
        #SOL 2(MOST OPTIMAL)
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res