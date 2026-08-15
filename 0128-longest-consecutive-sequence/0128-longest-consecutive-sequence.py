class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        nums=list(sorted(set(nums)))
        print(nums)
        i=0
        j=1
        maxi=1
        while(j<len(nums)):
            if nums[j]!=nums[j-1]+1:
                i=j
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi