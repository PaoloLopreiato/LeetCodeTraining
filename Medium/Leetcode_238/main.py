#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]

nums = [1,2,3,4]

def main():
    print(p_self_0(nums))


#Works but is not in O(n) time
def p_self_0(nums):
    result = []
    for i in range(len(nums)):
        tmp = 1
        for j in range(len(nums)):
            if j == i:
                pass
            else:
                tmp *= nums[j]
        result.append(tmp)
    return result

#O(n) time
def p_self_0(nums):
    result = [1]*(len(nums))

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix = prefix*nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i]*postfix
        postfix = postfix*nums[i]
    return result
    
if __name__ == "__main__":
    main()