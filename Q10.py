2154. Keep Multiplying Found Values by Two


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        return self.findFinalValue(nums, original*2)
