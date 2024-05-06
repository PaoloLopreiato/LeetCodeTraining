class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob(num):
            rob1, rob2 = 0, 0 
            
            for n in num:
                tmp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2

        return max(rob(nums[:len(nums) -1]), rob(nums[1:]))