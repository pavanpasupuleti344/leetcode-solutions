class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        i=k
        while 1:
            if i in s:
                i+=k
            else:
                return i