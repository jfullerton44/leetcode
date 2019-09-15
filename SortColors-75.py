class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}
        for element in nums:
            if element in colors:
                colors[element]= colors[element]+1
            else:
                colors[element]=1
        i=0
        if 0 in colors:
            elem = colors[0]
            while elem > 0:
                nums[i]= 0
                elem-=1
                i+=1
        if 1 in colors:
            elem = colors[1]
            while elem > 0:
                nums[i]= 1
                elem-=1
                i+=1
        if 2 in colors:
            elem = colors[2]
            while elem > 0:
                nums[i]= 2
                i+=1
                elem-=1
