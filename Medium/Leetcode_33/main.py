nums = [4,5,6,7,0,1,2]
target = 1

def main():
    print(search_rotated_sorted_array_1(nums, target))
    
def search_rotated_sorted_array_0(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1          
        else:
            right = mid
    r_point = left
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        r_mid = (mid + r_point) %len(nums)
        
        if target == nums[r_mid]:
            return r_mid
        elif target > nums[r_mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search_rotated_sorted_array_1(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1       
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1   

if __name__ == "__main__":
    main()