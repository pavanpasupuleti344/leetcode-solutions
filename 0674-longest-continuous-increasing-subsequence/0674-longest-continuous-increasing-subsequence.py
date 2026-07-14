class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        last=nums[0]
        ans=1
        c=1
        for i in range(1,len(nums)):
            if c==0 or nums[i]>last:
                c=c+1
                last=nums[i]
            else:
                ans=max(ans,c)
                c=1
                last=nums[i]
        return max(ans,c)
