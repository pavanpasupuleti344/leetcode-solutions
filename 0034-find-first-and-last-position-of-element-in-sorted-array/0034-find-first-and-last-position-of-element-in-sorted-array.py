class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fi=-1
        li=-1
        i=0
        j=len(nums)-1
        m=i+((j-i//2))
        while i<=j:
            if nums[m]==target:
                fi=m
                j=m-1
                m=i+((j-i//2))
            elif nums[m]>target:
                j=m-1
                m=i+((j-i//2))
            else:
                i=m+1
                m=i+((j-i//2))
        i=0
        if(fi!=-1):
            li=fi
            i=fi+1
        j=len(nums)-1
        m=i+((j-i)//2)
        while i<=j:
            if nums[m]==target:
                li=m
                i=m+1
                m=i+((j-i)//2)
            elif nums[m]>target:
                j=m-1
                m=i+((j-i)//2)
            else:
                i=m+1
                m=i+((j-i)//2)
        return [fi,li]