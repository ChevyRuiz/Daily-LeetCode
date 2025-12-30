import math
class PointAndDistance:
    def __init__(self, point):
        self.distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        self.point = point
    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        ans = []
        for point in points:
            minHeap.append(PointAndDistance(point))
        heapq.heapify(minHeap)
        for i in range(k):
            ans.append(heapq.heappop(minHeap).point)
        return ans
