class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        n=len(height)
        i=0
        j=n-1
        while i<j:
            c_w=j-i
            c_h=min(height[i],height[j])
            current_area=(c_w)*(c_h)
            max_water=max(current_area,max_water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water


        