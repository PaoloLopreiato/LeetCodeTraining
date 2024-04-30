class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #HEAP SOLUTION
        heapq.heapify(nums)

        K = len(nums) - k + 1
        res = 0
        for i in range(K):
            res = heapq.heappop(nums)
        return res
    
        #NO SHIT
        #nums.sort()
        #return nums[len(nums) - k]
        
        #SOLUTION(Quick Select)
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]
            
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
            
        return quickSelect(0, len(nums) - 1)