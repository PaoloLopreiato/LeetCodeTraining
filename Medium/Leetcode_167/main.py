#Input: numbers = [2,3,4], target = 6
numbers = [2,3,4]
target = 6

def main():
    #print(two_sum_0(numbers,target))
    print(two_sum_1(numbers,target))

#WORKS BUT SHIT O(n^2)
def two_sum_0(numbers,target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i and (numbers[i] + numbers[j]) == target:
                return [i+1,j+1]

#MOST OPTIMAL O(n)
def two_sum_1(numbers,target):
    i, j = 0, (len(numbers) - 1)
    while i < j:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            return [i + 1, j + 1]  
      
if __name__ == "__main__":
    main()