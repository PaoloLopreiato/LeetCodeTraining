"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]

def main():
    print(trapping_rain_water_1(height))

def trapping_rain_water_0(height):
    
    trapped_water = 0
    n = len(height)
    maxL = [0] * n
    maxR = [0] * n
    
    maxL[0] = height[0]
    for i in range(1, n):
        maxL[i] = max(maxL[i-1], height[i])
    
    maxR[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        maxR[i] = max(maxR[i+1], height[i])
        
    for i in range(n):
        trapped_water += min(maxL[i], maxR[i]) - height[i]  
    
    return trapped_water

def trapping_rain_water_1(height):
    
    if not height:
        return 0
      
    trapped_water = 0 
    l, r = 0, len(height) - 1
    maxL, maxR = height[l], height[r]
    
    while l <= r:
        if maxL < maxR:
            l += 1
            maxL = max(maxL, height[l])     
            trapped_water += min(maxL, maxR) - height[l]
        else:
            r -= 1
            maxR = max(maxR, height[r])
            trapped_water += min(maxL, maxR) - height[r]
            
    return trapped_water
    
if __name__ == "__main__":
    main()