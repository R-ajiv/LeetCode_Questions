242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        return l1==l2
