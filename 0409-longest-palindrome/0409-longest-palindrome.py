class Solution:
    def longestPalindrome(self, s: str) -> int:
        x=set()
        length=0
        for i in s:
            if i in x:
                x.remove(i)
                length+=2
            else:
                x.add(i)
        if x:
            length+=1
        return length