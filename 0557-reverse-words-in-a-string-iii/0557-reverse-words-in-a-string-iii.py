class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        # r=list(map(lambda s:"".join(reversed(s)),l))
        r=list(map(lambda s:s[::-1],l))
        return " ".join(r)
