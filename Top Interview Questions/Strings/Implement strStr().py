class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if l == 0 :
            return 0
        else:
            x = haystack.find(needle)
            return x
