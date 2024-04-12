s1 = "ab"
s2 = "eidbaooo"

def main():
    print(string_permutation_1(s1,s2))

#ASH O(n*26) SIUUUU
def string_permutation_0(s1,s2):
    if len(s1) > len(s2):
        return False
    
    ash_s1 = {}
    ash_s2 = {}
    
    for i in range(len(s1)):
        ash_s1[s1[i]] = ash_s1.get(s1[i], 0) + 1
        ash_s2[s2[i]] = ash_s2.get(s2[i], 0) + 1
      
    l, r = 0, len(s1) - 1
    
    while r < len(s2):
        if ash_s1 == ash_s2:
            return True
        
        r += 1
        if r < len(s2):
            ash_s2[s2[r]] = ash_s2.get(s2[r], 0) + 1
            ash_s2[s2[l]] -= 1
            if ash_s2[s2[l]] == 0:
                del ash_s2[s2[l]]
            l += 1
    return False
#O(n)
def string_permutation_1(s1,s2):     
    if len(s1) > len(s2):
        return False
    
    s1_count, s2_count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1
    
    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        index = ord(s2[r]) - ord('a')
        s2_count[index] += 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1
        
        index = ord(s2[l]) - ord('a')
        s2_count[index] -= 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1
        l += 1
    return False
        
        
        

if __name__ == "__main__":
    main()