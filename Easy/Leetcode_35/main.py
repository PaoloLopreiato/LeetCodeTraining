"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""
nums = [1,3,5,6] 
target = 2

def main():
    print(search_insert_position(nums, target))
    print(search_i_position(nums, target))

#Even better
def search_i_position(nums, target):
    if target in nums:
        return nums.index(target)
    
    #banalmenete aggiungo il target alla lista faccio un sort e bom prendo l'index doce é presente il target
    nums.append(target)
    nums.sort()
    return nums.index(target)

#My solution
def search_insert_position(nums, target):
    if target in nums:
        return nums.index(target)
    
    if target < nums[0]:
        return 0
    
    if target > nums[len(nums) - 1]:
        return len(nums)
    
    for i in range(len(nums)- 1):
        if nums[i] < target and target < nums[i+1]:
            return i+1   

if __name__ == "__main__":
    main()