nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]

def main():
    print(most_frequent(nums, k))

def most_frequent(nums, k):
    tmp = {}
    result = []
    for i in nums:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1
    j = 0
    while j < k:
        maxF = max(tmp.values())
        maxK = []
        for key, value in tmp.items():
            if value == maxF:
                maxK.append(key)
                j += 1
        result.extend(maxK)
        for key in maxK:
            del tmp[key]
    return result
    
if __name__ == "__main__":
    main()