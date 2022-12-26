2278. Percentage of Letter in String

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
#         c=0
#         for i in letter:
#             if i in s:
        c=s.count(letter)
        return c*100//len(s)
