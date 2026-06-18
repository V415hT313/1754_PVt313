class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        totalWater = 0 
        while start <= end:
            waterQ = min(heights[start],heights[end]) * (end-start)
            totalWater = max(totalWater, waterQ)
            if heights[start] < heights[end]:
                start+= 1
            elif heights[start] >= heights[end]:
                end-= 1
            # else heights[start] = heights[end]:

        return totalWater
            

        