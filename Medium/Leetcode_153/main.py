nums = [11,13,15,17]

def main():
    print(min_rotated_sorted_1(nums))

#No SHIT, But not optimal 
def min_rotated_sorted_0(nums):
    return min(nums)
    
def min_rotated_sorted_1(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1          
        else:
            right = mid
    return nums[left]
    
    
if __name__ == "__main__":
    main()