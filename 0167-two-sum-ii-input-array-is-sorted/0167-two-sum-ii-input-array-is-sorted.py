class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        i=0
        j=len(nums)-1
        while(i<j):
            s=nums[i]+nums[j]
            if s==target:
                return [i+1,j+1]
                # l.append(i+1)
                # l.append(j+1)
                # break
            elif(s>target):
                j-=1
            else:
                i+=1
        return []