class Solution:
    def countSubstrings(self, s: str) -> int:
        lenS = len(s)
        res = 0
        for i in range(lenS):
            #Even case
            l,r = i,i
            while l >= 0 and r < lenS and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            #Odd case
            l,r = i,i+1
            while l >= 0 and r < lenS and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res