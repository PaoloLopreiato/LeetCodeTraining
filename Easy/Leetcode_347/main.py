nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]

def main():
    print(most_frequent_0(nums, k))
    print(most_frequent_1(nums, k))


#MY SOLUTION
def most_frequent_0(nums, k):
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
    #This also would work
    #sorted_dict_values_desc = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
    #for key, _ in sorted_dict_values_desc[:k]:
    #   result.append(key)     

#SOLUTION 2
def most_frequent_1(nums, k):
    array = [[]for i in range(len(nums) + 1)]
    ashmap = {}
    result = []
    for n in nums:
        ashmap[n] = 1 + ashmap.get(n, 0)
    for n, c in ashmap.items():
        array[c].append(n) #ARRAY C INDICA IL NUMERO DI VOLTE L'elemento N é presente
    for i in range(len(array) - 1, 0, -1):
        for n in array[i]:
            result.append(n)
            if len(result) == k:
                return result

if __name__ == "__main__":
    main()