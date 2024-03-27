s = "anagram" 
t = "nagaram"

def main():
    print(is_valid_anagram(s, t))

def is_valid_anagram(s, t):
    if sorted(s) == sorted(t):
        return True
    return False

if __name__ == "__main__":
    main()