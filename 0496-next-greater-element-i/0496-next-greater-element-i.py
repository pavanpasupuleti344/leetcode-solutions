class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans=[-1]*len(nums1)
        d={}
        stack=[]
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                # ans[stack[-1]]=nums2[i]
                d[nums2[stack[-1]]]=nums2[i]
                stack.pop()
            stack.append(i)
        # print(d)
        ans=[]
        for i in nums1:
            ans.append(d.get(i,-1))
        # print(ans)
        return ans
        # print(ans)
        # d={}
        # for i in range(ans):
        #     d[nums2[i]]=ans[i]
