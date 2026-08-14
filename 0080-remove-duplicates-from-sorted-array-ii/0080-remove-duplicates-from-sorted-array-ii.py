class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        j=0
        while(j<len(nums)):
            d[nums[j]]=d.get(nums[j],0)+1
            while 3 in d.values():
                d[nums[j]]-=1
                nums.pop(j)
                j-=1
            j+=1
        return len(nums)