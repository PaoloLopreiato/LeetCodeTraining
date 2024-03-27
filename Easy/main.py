nums = [1,1,1,3,3,4,3,2,4,2]

def main():
    print(contains_duplicate(nums))

def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
    
if __name__ == "__main__":
    main()