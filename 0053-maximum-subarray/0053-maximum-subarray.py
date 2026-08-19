class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi=maxi=nums[0]
        j=1
        while j<len(nums):
            if sumi<0:
                sumi=nums[j]
            else:
                sumi+=nums[j]
            j+=1
            maxi=max(maxi,sumi)
        return maxi