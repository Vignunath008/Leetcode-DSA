class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        n=len(height)
        i=0
        j=n-1
        while i<n and j>0:
            c_w=j-i
            c_h=min(height[i],height[j])
            current_area=(c_w)*(c_h)
            max_water=max(current_area,max_water)
            if height[i]<height[j]:
                i+=1
            elif height[j]<=height[i]:
                j-=1
        return max_water


        