class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # pmax=smax=pc=sc=nums[0]
        pc=sc=1
        pmax=smax=-10**100
        # if pc==0:pc=1
        # if sc==0:sc=1
        for i in range(len(nums)):
            pc*=nums[i]
            sc*=nums[len(nums)-i-1]
            pmax=max(pmax,pc)
            smax=max(smax,sc)
            if pc==0:
                pc=1
            if sc==0:
                sc=1
        return max(pmax,smax)