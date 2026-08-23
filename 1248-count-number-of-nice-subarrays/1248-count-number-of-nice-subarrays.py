class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        start=0
        ans=0
        l=[]
        for i in range(len(nums)):
            if nums[i]&1!=0:
                l.append(i)
            if len(l)==k:
                ans+=l[0]-start+1
            elif len(l)>k:
                start=l[0]+1
                l.pop(0)
                ans+=l[0]-start+1
        return ans

            