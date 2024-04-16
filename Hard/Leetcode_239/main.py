import collections

nums = [1,3,-1,-3,5,3,6,7]
k = 3

def main():
    print(sliding_window_maximum_1(nums, k))

#Works but Time limit Exeeded  O(k*(n - k))
def sliding_window_maximum_0(nums, k):
    maxwindow = []
    l = 0
    for r in range((k - 1),len(nums)):
        maxwindow.append(max(nums[l:r+1]))
        l += 1
    return maxwindow

#O(n)
def sliding_window_maximum_1(nums, k):
    output = []
    q = collections.deque()
    l, r = 0, 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
           q.pop() 
        q.append(r)
        
        if l > q[0]:
            q.popleft()
            
        if r + 1 >= k:
            output.append(nums[q[0]])
            l += 1          
        r += 1
        
    return output
    
if __name__ == "__main__":
    main()