class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]  # Use negative values for max heap simulation
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first_largest = -heapq.heappop(maxHeap)  # Get the largest element
            second_largest = -heapq.heappop(maxHeap)  # Get the second largest element
            
            if first_largest != second_largest:
                difference = first_largest - second_largest
                heapq.heappush(maxHeap, -difference)  # Push negative of difference for max heap
        
        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0] 