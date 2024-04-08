import math

#Input: piles = [3,6,7,11], h = 8
#Output: 4
piles = [3,6,7,11]
h = 8

def main():
    print(koko_eating_bananas_0(piles, h))

def koko_eating_bananas_0(piles, h):
    #if h == len(piles):
        #return max(piles)
    l, r = 1, max(piles)
    res = r   
    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1      
    return res
            
if __name__ == "__main__":
    main()