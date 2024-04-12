s = "ADOBECODEBANC"
t = "ABC"

def main():
    print(minimum_window_substring_0(s, t))

def minimum_window_substring_0(s, t):
    if t == "": return ""
    
    countT, window = {}, {}
    
    for c in t:
        countT[c] = countT.get(c, 0) + 1
        
    have, need = 0, len(countT)
    
    l = 0
    res, resl = [-1, -1], float("inf")
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1
        
        if c in countT and window[c] == countT[c]:
            have += 1
        
        while have == need:
            if (r - l + 1) < resl:
                res = [l, r]
                resl = r - l + 1
            window[s[l]] -= 1
            if s[l] in countT and  window[s[l]] < countT[s[l]]:            
                have -= 1
            l += 1
    l, r = res
    if resl != float("inf"):
        return s[l:r+1]
    else:
        return ""

if __name__ == "__main__":
    main()