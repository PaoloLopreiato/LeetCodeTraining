"""
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""
#nums1 = [1,3]
#nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]

def main():
    #print(median_two_sorted_array_0(nums1,nums2))
    print(median_two_sorted_array_1(nums1,nums2))

#Works but is Dogshit O(n+m)
def median_two_sorted_array_0(nums1,nums2):
    ma = []
    for i in nums1:
        ma.append(i)
    for i in nums2:
        ma.append(i)
    ma = sorted(ma)
    if len(ma) % 2 == 1:
        return ma[len(ma)%2]
    else:
        media = (ma[len(ma) // 2] + ma[(len(ma) // 2) - 1]) / 2
        return media

def median_two_sorted_array_1(nums1,nums2):
    a, b = nums1, nums2
    total = len(a) + len(b)
    half = total // 2

    if len(b) < len(a):
        a, b = b, a
    
    left, right = 0, len(a) - 1
    while True:
        i = (left + right) // 2
        j = half - i - 2
        

        aleft = a[i] if i >= 0 else float("-infinity")
        aright = a[i + 1] if (i + 1) < len(a) else float("infinity")
        bleft = b[j] if j >= 0 else float("-infinity")
        bright = b[j + 1] if (j + 1) < len(b) else float("infinity")

        if aleft <= bright and bleft <= aright:
            if total % 2:  
                return min(aright, bright)
            else:  
                return (max(aleft, bleft) + min(aright, bright)) / 2
        elif aleft > bright:
            right = i - 1
        else:
            left = i + 1
            
if __name__ == "__main__":
    main()