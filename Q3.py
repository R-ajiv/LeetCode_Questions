# 2042. Check if Numbers Are Ascending in a Sentence

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a=s.split(' ')
        n=[]

        for i in a:
            if i.isnumeric():
                n.append(int(i))

        for i in range(1,len(n)):
            if n[i]<=n[i-1]:
                return False

        return True