class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        y=[]
        freq={}
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        for j in nums2:
            if j in freq and freq[j]>0:
                y.append(j)
                freq[j]-=1
        return y
        
        
                
            
                

        