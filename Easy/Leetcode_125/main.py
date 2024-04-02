import re

s = "A man, a plan, a canal: Panama"

def main():
    print(valid_palindrome_0(s))

def valid_palindrome_0(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if s == " ":
        return False
    j = len(s) - 1
    i = 0
    while i < (len(s) / 2):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def valid_palindrome_1(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if s == " ":
        return False
    return s == s[::-1]

if __name__ == "__main__":
    main()