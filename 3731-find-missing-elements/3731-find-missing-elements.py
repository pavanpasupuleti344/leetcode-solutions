class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # totalsum=sum(nums)
        l=[]
        mini=min(nums)
        maxi=max(nums)
        for i in range(mini+1,maxi):
            if i not in nums:
                l.append(i)
        return l
        # tot=(maxi*(maxi+1)//2)-((mini-1)*(mini)//2)
        # if tot-totalsum == 0:
        #     return[]
        # else:
        #     return [tot-totalsum]