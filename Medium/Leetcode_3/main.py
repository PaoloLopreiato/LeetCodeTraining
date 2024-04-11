s = "abcabcbb"

def main():
    print(longest_sub_no_repeating_1(s))

#Works   
def longest_sub_no_repeating_0(s):
    longest, current = 0, 0
    stack = []
    for c in s:
        if c in stack:
            stack.clear()
            stack.append(c)
            longest = max(longest, current)
            current = 1       
        else:
            stack.append(c)
            current += 1
    return longest

def longest_sub_no_repeating_1(s):
    substring = set()
    left = 0
    result = 0
    
    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left += 1
        substring.add(s[right])
        result = max(result, len(substring))
    return result

if __name__ == "__main__":
    main()