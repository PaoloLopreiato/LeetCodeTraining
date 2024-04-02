#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]

def main():
    print(three_sum_0(nums))

def three_sum_0(nums):
    output = []
    nums = sorted(nums)
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                output.append([nums[i], nums[j], nums[k]])
                # Skip duplicates
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1
    return output
            
if __name__ == "__main__":
    main()