class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=[]
        i=0
        j=0
        tl=len(nums1)+len(nums2)
        m1=m2=-1
        if tl&1==0:
            m1=tl//2
            m2=m1-1
        else:
            m1=m2=(tl//2)
        while i<len(nums1) and j<(len(nums2)):
            if nums1[i]<=nums2[j]:
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
        ans+=nums1[i:]+nums2[j:]
        return (ans[m1]+ans[m2])/2
