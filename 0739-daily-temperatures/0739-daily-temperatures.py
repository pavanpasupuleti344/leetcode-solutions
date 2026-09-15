class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        # stack=[0]*len(nums)
        stack=[]
        ans=[0]*len(nums)
        for i in range(len(nums)):
            while  len(stack)>0 and nums[i]>nums[stack[-1]]:
                ans[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans