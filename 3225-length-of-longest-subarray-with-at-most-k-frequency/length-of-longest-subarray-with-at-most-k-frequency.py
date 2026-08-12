class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        i=0
        j=0
        maxi=1
        while(j<len(nums)):
            d[nums[j]]=d.get(nums[j],0)+1
            while d[nums[j]]>k:
                d[nums[i]]-=1
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        print(d)
        return maxi
        