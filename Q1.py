# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        l=len(nums)
        x=[]
        c=0
        for i in nums:
            for j in range(l):
               if (nums[j]-i)<0:
                   c+=1
            x.append(c)
            c=0
        return x
        