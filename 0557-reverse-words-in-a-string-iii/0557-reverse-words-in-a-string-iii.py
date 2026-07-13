class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        r=list(map(lambda s:"".join(reversed(s)),l))
        return " ".join(r)
