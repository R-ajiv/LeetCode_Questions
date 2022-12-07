# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[i*i for i in nums]
        return sorted(output)
        