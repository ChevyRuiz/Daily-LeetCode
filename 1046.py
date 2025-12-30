class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            y = - heapq.heappop(maxHeap)
            x = - heapq.heappop(maxHeap)
            if x != y:
                y = y - x
                heapq.heappush(maxHeap, -y)
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
