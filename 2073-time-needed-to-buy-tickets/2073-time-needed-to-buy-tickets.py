class Solution:
    def timeRequiredToBuy(self, nums: list[int], k: int) -> int:
        q=[i for i in range(len(nums))]
        # print(q)
        ans=0
        while nums[k]!=0:
            nums[q[0]]-=1
            if nums[q[0]]==0:
                q.pop(0)
            else:
                q.append(q[0])
                q.pop(0)
            ans+=1
        return ans

            