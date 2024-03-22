nums = [0,0,1,1,1,2,2,3,3,4]

def main():
    #print(cheker(nums))
    print(cheker_b(nums))

def cheker(nums):
    k = 0
    numsT = []
    for i in nums:
        if i not in numsT:
            numsT.append(i)
            k += 1
    return k

def cheker_b(nums):
    if not nums:
        return 0

    j = 0  
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    k = j + 1
    return k


if __name__ == "__main__":
    main()