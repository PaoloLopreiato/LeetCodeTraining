"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
height = [2,3,4,5,18,17,6]

height = [2, 3, 4, 5, 18, 17, 6]

def main():
    print(container_with_most_water_0(height))

#My solution
def container_with_most_water_0(height):
    i, j = 0, (len(height) - 1)
    maxArea = 0
    while i < j:
        heightM = min(height[i], height[j])
        Base = j - i
        maxArea = max(maxArea, heightM * Base)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxArea

#Official Sol()


if __name__ == "__main__":
    main()