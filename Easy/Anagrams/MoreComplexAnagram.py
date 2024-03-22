strs = ["eat","tea","tan","ate","nat","bat"]
#otput = [[]]

def main():
    print(anagram_checker(strs))

def anagram_checker(strs):
    anagrams = {}
    sorted_str = ""
    for i in strs:
        sorted_str = "".join(sorted(i))#Join Because Sorted gives back a list but with join i can get a string
        
        if sorted_str in anagrams:
            anagrams[sorted_str].append(i) #Se la versione ordinata esiste giá in anagramma aggiungo ad esse un value equivalente alla str non sorted
        else:
            anagrams[sorted_str] = [i] # se l'anagramma non esiste lo aggiungo come nuova chiave l'anagramma e come valore i

    return list(anagrams.values())
            
if __name__ == "__main__":
    main()