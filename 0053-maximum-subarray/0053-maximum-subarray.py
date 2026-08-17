class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi=nums[0]
        maxi=sumi
        for i in range(1,len(nums)):
            if sumi<0:
                sumi=nums[i]
                maxi=max(maxi,sumi)
            else:
                sumi+=nums[i]
                maxi=max(maxi,sumi)
        return maxi