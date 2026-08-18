class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        i=0
        j=0
        maxi=0
        while j<len(s):
            while i<=j and s[j] in d:
                d.remove(s[i])
                i+=1
            else:
                d.add(s[j])
                maxi=max(maxi,j-i+1)
                j+=1
        return maxi
            