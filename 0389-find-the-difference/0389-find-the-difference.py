class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq={}
        freq1={}
        for i in t:
            freq[i]=freq.get(i,0)+1
        for j in s:
            freq1[j]=freq1.get(j,0)+1
        for x in freq:
            if freq.get(x)!=freq1.get(x):
                return x
        