nums = [3,1,3,4,2]

def main():
    print(repeated_numbers_0(nums))

#Done without using set (nightmare) Floyd Hare
def repeated_numbers_0(nums):
    s, f = 0, 0
    while True:
        s = nums[s]
        f = nums[nums[f]]
        if s == f:
            break
    
    s2 = 0
    while True:
        s = nums[s]
        s2 = nums[s2]
        if s == s2:
            return s
    
#Done CHEATING O(n) BUT USING A SET()
def repeated_numbers_1(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    return None

if __name__ == "__main__":
    main()