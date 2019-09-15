class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 0:
            return 0
        leftMax = [None] * size
        leftMax[0]=height[0]
        rightMax = [None] * size
        rightMax[size-1]=height[size-1]
        water=0
        for i in range(1,size):
            leftMax[i]= max(leftMax[i-1],height[i])
            rightMax[size-i-1] = max(rightMax[size-i],height[size-i-1])
        for i in range(1,size):
            water += min(leftMax[i],rightMax[i])-height[i]
        return water
            