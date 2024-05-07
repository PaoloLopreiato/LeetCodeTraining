class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        res = ""
        for i in range(len(s)):
            # Odd-length palindrome
            j, k = i - 1, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            odd_palindrome = s[j + 1:k]

            # Even-length palindrome
            j, k = i, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            even_palindrome = s[j + 1:k]

            if len(odd_palindrome) > len(res):
                res = odd_palindrome
            if len(even_palindrome) > len(res):
                res = even_palindrome
                
        return res
