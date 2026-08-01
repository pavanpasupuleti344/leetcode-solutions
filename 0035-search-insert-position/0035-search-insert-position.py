class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        m=i+((j-i)//2)
        while i<=j:
            if target==nums[m]:return m
            elif nums[m]>target:
                j=m-1
                m=i+((j-i)//2)
            elif nums[m]<target:
                i=m+1
                m=i+((j-i)//2)
        return i
            