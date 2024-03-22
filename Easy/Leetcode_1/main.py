"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
nums = [2,7,11,15]
target = 22

def main():
    print(sum_index(nums, target))

def sum_index(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                if target - (nums[i] + nums[j]) == 0:
                    output = [i, j]
                    return output

if __name__ == "__main__":
    main()