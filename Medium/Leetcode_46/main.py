class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    
#Option 2        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def prm(used, perm):
            if len(perm) == len(nums):
                perms.append(perm.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    perm.append(nums[i])
                    prm(used, perm)
                    used.remove(nums[i])
                    perm.pop()
        
        prm(set(), [])
        return perms