"""
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
nums = [0,1,2,2,3,0,4,2]
val = 2

def main():
    print(replace_values(nums,val))
"""
def replace_values(nums, val):
    k = 0
    for i, num in enumerate(nums):
        if num == val:
            nums[i] = nums[i+1]
            k += 1
    return k
"""
def replace_values(nums, val):
    k = 0
    i = 0
    #If the array is empty i return none
    if not nums:
        return k
  
    while i < len(nums) -1:
        if nums[i] == val:
            #Sovrascrivo il valore uguale con il valore successivo
            nums[i] = nums[i+1]
            k += 1
            for j in range(i+1, len(nums) -1):
                #sostituisco tutti i valori successivi al valore che ho sostituito con il loro valore successivo
                nums[j] = nums[j+1]
            #al fondo della lista ho un volore duplicato che poppo [0,1,2,2,3,0,4,2] -- [0,1,2,3,0,4,2,2] -- [0,1,2,3,0,4,2]
            nums.pop()
        else:
            i += 1
    if nums[len(nums)-1] == val:
        k += 1
        nums.pop()
    #nums = nums[:k]
    return f"Output: {k}, nums = {nums}"
if __name__ == "__main__":
    main()