class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=(len(nums)+1)
        for i in range(len(nums)):
            if nums[i]>=target:return 1
            elif i==0:
                continue
            else:
                nums[i]=nums[i]+nums[i-1]
                if nums[i]>=target:
                    mini=min(mini,i+1)
        i=1
        j=i+1
        while(j<len(nums)):
            if j<i:
                j=i+1
            if (nums[j]-nums[i-1])>=target:
                mini=min(mini,j-i+1)
                i+=1
            else:
                j+=1
        if mini==len(nums)+1:
            return 0
        return mini