from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = (Counter(nums).most_common()[::-1][0][0])
        return m
