"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

def main():
    #prefix(strs)
    #print(common_prefix(strs))
    print(prefixes(strs))

"""
def prefix(strs):
    i = 0
    prefix = ""
    min_length = int('inf')  
    for word in strs:
        if len(word) < min_length:
            min_length = len(word)
    #for j in range(len(strs)):
        #for i in rage(min_length):
            #if strs[j][i] == strs[j][i] and strs[j][i] == strs[j][i]
    for word in strs:
        for char in word:
            if not prefix:
"""

def prefixes(strs):
    #Entering this loop gives me a character from the first word and a number for example 0 f 1 l et..
    for i, char in enumerate(strs[0]):
        #enter another loop to compare all word in array skipping the forst one ence[:1]
        for word in strs[1:]:
            #if i is shorter than the word it means that it could mach for example
            #"flower","flow" 5 e cant be compared with 5 ""
            #then it compares the caharacters for example 1 f == 1 f in that case i do
            #nothing because it means that is maching but if it doesn't mach then
            #i slice the first word strs[0] to the current i we reaceded ence [start to:i]
            if i <= len(word) and word[i] == char:
                pass
            else:
                return strs[0][:i]
    return "" #if nothing is found return ""


def common_prefix(strs):
    # Iterate through the characters of the first word in the list
    for i, char in enumerate(strs[0]):
        # Iterate through the words in the list, starting from the second word
        for word in strs[1:]:
            # If the current character does not match the corresponding character
            # in any other word, return the common prefix found so far
            if i >= len(word) or char != word[i]:
                return strs[0][:i]
    
    # If all characters in the first word match the corresponding characters
    # in all other words, return the first word itself as the common prefix
    return strs[0]
                
    



if __name__ == "__main__":
    main()