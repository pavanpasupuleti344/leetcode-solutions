class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxi=0
        d={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            if i!=0:
                nums[i]+=nums[i-1]
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                maxi=max(maxi,i-d.get(nums[i]))
            # print(d)
        return maxi
            
