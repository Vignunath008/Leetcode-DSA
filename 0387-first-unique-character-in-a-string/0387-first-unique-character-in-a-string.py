class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=""
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq.get(i)==1:
                a+=(i)
                break
        for i in range(len(list(s))):
            if a ==s[i]:
                return i
        else:
            return -1

                 


        