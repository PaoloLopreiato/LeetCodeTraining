class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        ash = { 
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, cur):
            if len(cur) == len(digits):  # Check length of cur against length of digits
                res.append(cur)
                return
            for c in ash[digits[i]]:  # Use digits[i] to get the current digit character
                backtrack(i + 1, cur + c)
       
        if digits:
            backtrack(0, "")  # Start backtracking with initial parameters
        return res