nums = [-1,0,3,5,9,12]
target = 9

def main():
    print(binary_search(nums, target))

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

if __name__ == "__main__":
    main()
