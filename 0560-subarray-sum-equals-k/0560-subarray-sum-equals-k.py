class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        d={0:1}
        d[nums[0]]=d.get(nums[0],0)+1
        if nums[0]==k:c+=1
        for i in range(1,len(nums)):
            # if nums[i]==k:
            #     c+=1
            # else:
            nums[i]+=nums[i-1]
            # if nums[i]==k:c+=1
            req=nums[i]-k
            c+=d.get(req,0)
            d[nums[i]]=d.get(nums[i],0)+1
        return c
