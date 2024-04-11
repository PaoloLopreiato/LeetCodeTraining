s = "ABAB"
k = 2

def main():
    print(l_repeating_c_r_1(s,k))

#Hard, Works O(26)
def l_repeating_c_r_0(s, k):
    res = 0
    ash = {}  
    left = 0
    
    for right in range(len(s)):
        ash[s[right]] = 1 + ash.get(s[right], 0)
        while (right - left + 1) - max(ash.values()) > k:
            ash[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    
    return res

#Fukking Demonic O(n)
def l_repeating_c_r_1(s, k):
    res = 0
    ash = {}  
    left = 0
    
    maxf = 0
    for right in range(len(s)):
        ash[s[right]] = 1 + ash.get(s[right], 0)
        maxf = max(maxf, ash[s[right]])
        while (right - left + 1) - maxf > k:
            ash[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    
    return res

    
"""
def l_repeating_c_r_0(s, k):
    res, tmp = 0, k
    left, right = 0, 1
    stack = []
    while right < len(s):
        while tmp >= 0:
            if s[left] == s[right]:
                stack.append(s[left])
                right += 1
            else:
                tmp -= 1
        res = max(res, len(stack))
        stack.clear()
        left += 1
        right = left + 1
        if tmp == -1:
            tmp = k
    return res
"""      
        
if __name__ == "__main__":
    main()