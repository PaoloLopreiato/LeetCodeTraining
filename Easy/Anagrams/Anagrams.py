#anagarms = ["bat", ""eat, ""tame, ""kill, ""lkki, ""tea, ""tae, "meta"]
s_a = "abca"
s_b = "abbc"

def main():
    if anagram_checker(s_b, s_a):
        print(f"{s_a} is an anagram of {s_b}.")
    else:
        print("Not an anagram")

def anagram_checker(a,b):
    check = True
    
    if len(a) != len(b):
        return False
    
    c_ash = {}
    for c in a:
        if c in c_ash:
            c_ash[c] += 1
        else:
            c_ash[c] = 1            
            
    for c in b:
        if c in c_ash:
            c_ash[c] -= 1
            if c_ash[c] < 0:
                return False    
            elif c_ash[c] != 0:
                check = False
            else:
                check = True
        else:
            return False
    return check
        
if __name__ == "__main__":
    main()