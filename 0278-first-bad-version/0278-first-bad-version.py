# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i=1
        j=n  
        m=i+((j-i)//2)
        while i<=j:
            if isBadVersion(m)==True:
                j=m-1
                m=i+((j-i)//2)
            elif isBadVersion(m)==False:
                i=m+1
                m=i+((j-i)//2)
        return i