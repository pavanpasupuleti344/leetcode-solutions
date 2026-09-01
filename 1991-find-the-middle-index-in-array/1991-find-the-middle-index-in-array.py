class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre=[0]*len(nums)
        pre[0]=nums[0]
        suf=[0]*len(nums)
        suf[-1]=nums[-1]
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]+nums[i]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]+nums[i]
        # print(pre,suf)
        for i in range(len(nums)):
            if i==0:
                left=0
            else:
                left=pre[i-1]
            if i==len(nums)-1:
                right=0
            else:
                right=suf[i+1]
            if left==right:return i
        return -1
        