class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        ans=0
        for i in nums:
            if i==1:
                c=c+1
            else:
                ans=max(ans,c)
                c=0
        return max(ans,c)
