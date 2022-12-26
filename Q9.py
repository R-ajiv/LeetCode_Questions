2404. Most Frequent Even Element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in d:
                    d[nums[i]] += 1
                else:
                    d[nums[i]] = 1
                    
        l = list(d.keys())
        l.sort()
        
        answer = -1
        maxCount = 0
        for i in l:
            maxCount = max(maxCount, d[i])
        
        for i in l:
            if d[i] == maxCount:
                return i
        
        return answer
