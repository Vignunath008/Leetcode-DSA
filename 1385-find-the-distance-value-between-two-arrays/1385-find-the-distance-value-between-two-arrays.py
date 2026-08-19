class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        i=0
        x=0
        count=0
        while i<len(arr1):
            j=0
            valid=True
            while j<len(arr2):
                x=abs(arr1[i]-arr2[j])
                if x<=d:
                    valid=False
                    break
                j+=1
            if valid:
                count+=1
            i+=1
            
        return count



        