class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s=set()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:continue
                left=j+1
                right=len(nums)-1
                # print(nums[i:right+1])
                while(left<right):
                    sumi=nums[i]+nums[left]+nums[right]+nums[j]
                    if sumi==target:
                        print(nums[i:right+1])
                        s.add((nums[i],nums[left],nums[right],nums[j]))
                        left+=1
                        right-=1
                    elif sumi>target:
                        right-=1
                    elif sumi<target:
                        left+=1
        return list(s)