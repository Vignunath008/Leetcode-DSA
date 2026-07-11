class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=len(needle)
        for i in range(len(haystack)):
            if needle in haystack[i:i+x]:
                return i
                break
        return -1
        