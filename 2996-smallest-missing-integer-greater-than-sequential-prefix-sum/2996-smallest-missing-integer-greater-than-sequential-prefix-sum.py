class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sumi=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                sumi+=nums[i]
            else:
                break
        s=set(nums)
        while sumi in nums:
            sumi+=1
        return sumi