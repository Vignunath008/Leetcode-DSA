class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        freq1={}
        for i in ransomNote:
            freq[i]=freq.get(i,0)+1
        for j in magazine:
            freq1[j]=freq1.get(j,0)+1
        for i in freq:
            if freq.get(i)>freq1.get(i,0):
                return False
        return True
        