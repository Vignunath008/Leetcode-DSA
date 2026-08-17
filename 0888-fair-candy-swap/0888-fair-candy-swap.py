class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A=sum(aliceSizes)
        B=sum(bobSizes)
        diff=(A-B)//2
        bob_set=set(bobSizes)
        for x in aliceSizes:
            y=x-diff
            if y in bob_set:
                return [x,y]


        