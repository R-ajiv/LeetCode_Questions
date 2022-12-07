# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d={}
        for i in range(len(allowed)):
            d[allowed[i]]=1
        count=0

        for word in  words:
            consistent=True
            for ch in word:
                if ch not in d:
                    consistent=False

            if consistent ==True:
                count+=1
        return count
