class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi=[0]*len(nums)
        mini=[0]*len(nums)
        maxi[0]=nums[0]
        mini[len(mini)-1]=nums[len(nums)-1]
        for i in range(1,len(nums)):
            maxi[i]=max(maxi[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])
        ans=[0]*len(nums)
        # ans=sys.maxsize
        for i in range(len(nums)):
            ans[i]=maxi[i]-mini[i]
        small=ans[0]
        pos=0
        if small<=k:return 0
        for i in range(1,len(ans)):
            if ans[i]<small:
                small=ans[i]
                pos=i
                if small<=k:
                    return pos
        if small<=k:
            return pos
        else:
            return -1