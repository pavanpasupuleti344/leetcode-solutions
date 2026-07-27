class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        s=set()
        for i in range(0,(len(nums)-2)):
            t=0-(nums[i])
            j=i+1
            k=len(nums)-1
            while j<k:
                if ((nums[j]+nums[k])==t):
                    tu=(nums[i],nums[j],nums[k])
                    s.add(tu)
                    j+=1
                    k-=1
                elif ((nums[j]+nums[k])>t):
                    k-=1
                else:
                    j+=1
        return list(map(list,s))