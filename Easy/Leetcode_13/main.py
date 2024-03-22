s = "MCMXCIV"

def main():
    print(roman_n_converter(s))


def roman_n_converter(s):
    ashtbl = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
    result = 0
    now = 0
    last = 0
    #Iterate in reverse MCMXCIV starts from V because Roman numbers always start from the biggest to the smaller number
    for i in range(len(s) - 1, -1, -1):
        #Actual value = V in ashtbl wich is 5
        now = ashtbl[s[i]] 
        #if previus value is smaller than our currenbt value then we have to add
        if now >= last:
            result += now
        else:
        # I = 1 < V = 5 so 5 - 1 = 5 = CORRECT
            result -= now    
        last = now
    return result
        
    

if __name__ == "__main__":
    main()