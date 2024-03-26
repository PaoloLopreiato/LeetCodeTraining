#Input: nums = [100,4,200,1,3,2]
#Output: 4
nums = [0,3,7,2,5,8,4,6,0,1]

def main():
    #print(logest_sequence_0(nums))
    #print(logest_sequence_1(nums))
    print(logest_sequence_2(nums))


#My sol non O(n) Inperfect
def logest_sequence_0(nums):
    result = 1
    setnums = set()
    for i in nums:
        if i in setnums:
            continue
        else:
            setnums.add(i)
    sorted_setnums = sorted(setnums)
    for i in range(len(sorted_setnums) - 1):
        if sorted_setnums[i+1] - sorted_setnums[i] == 1:
            result += 1
        else:
            return result
    return result

def logest_sequence_1(nums):
    nums_set = set(nums)
    longest_streak = 0
    
    for num in nums_set:
        if num - 1 not in nums_set:  # Start counting from the beginning of a sequence
            current_num = num
            current_streak = 1
            
            while current_num + 1 in nums_set:  # Continue counting consecutive numbers
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)  # Update longest streak
        
    return longest_streak

def logest_sequence_2(nums):
    nums_set = set(nums)
    longest_streak = 0
    for n in nums:
        if n - 1 not in nums:
            lengh = 0
            while n + lengh in nums_set:
                lengh += 1
            longest_streak = max(lengh, longest_streak)
    return longest_streak


if __name__ == "__main__":
    main()