# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid=0
        i=1
        j=n
        while i<=j:
            mid=i+(j-i)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res<0:
                j=mid
            else:
                i=mid+1
        # return i+(j-i)//2