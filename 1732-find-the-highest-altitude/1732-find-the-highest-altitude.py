class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=0
        for i in range(len(gain)):
            if i!=0:
                gain[i]+=gain[i-1]
            maxi=max(maxi,gain[i])
        return maxi