class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0,0,0]

        for num in nums:
            colors[num] = colors[num] + 1
        
        i = 0
        for index in range(len(colors)):
            for j in range(colors[index]):
                nums[i] = index
                i = i + 1
